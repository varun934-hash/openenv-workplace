from fastapi import FastAPI
from pydantic import BaseModel
from env import WorkplaceEnv
from models import Action

app = FastAPI()

env = WorkplaceEnv()


# ✅ Request format for step
class StepRequest(BaseModel):
    action_type: str
    task_id: int


# ✅ ROOT
@app.get("/")
def home():
    return {"message": "Workplace Decision Engine Running ✅"}


# ✅ REQUIRED: RESET API
@app.post("/reset")
def reset():
    obs = env.reset()

    return {
        "tasks": [task.dict() for task in obs.tasks]
    }


# ✅ REQUIRED: STEP API
@app.post("/step")
def step(request: StepRequest):
    action = Action(
        action_type=request.action_type,
        task_id=request.task_id
    )

    obs, reward, done, info = env.step(action)

    return {
        "tasks": [task.dict() for task in obs.tasks],
        "reward": reward,
        "done": done,
        "score": info["score"]
    }


# ✅ OPTIONAL DEMO (for your testing)
@app.get("/run-demo")
def run_demo():
    obs = env.reset()

    logs = ["START"]
    done = False

    while not done:
        for task in obs.tasks:
            if task.status == "completed":
                continue

            action = Action(action_type="complete", task_id=task.id)

            obs, reward, done, info = env.step(action)

            logs.append(
                f"STEP | action={action.action_type} | reward={reward:.2f} | score={info['score']:.2f}"
            )

            if done:
                break

    logs.append("END")
    logs.append(f"FINAL_SCORE: {info['score']:.2f}")

    return {"logs": logs}