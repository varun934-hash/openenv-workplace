from fastapi import FastAPI
from env import WorkplaceEnv
from models import Action

app = FastAPI()

env = WorkplaceEnv()


@app.get("/")
def home():
    return {"message": "Workplace Decision Engine is running 🚀"}


@app.post("/reset")
def reset():
    obs = env.reset()
    return obs.model_dump()


@app.post("/step")
def step(action: Action):
    obs, reward, done, info = env.step(action)
    return {
        "observation": obs.model_dump(),
        "reward": reward,
        "done": done,
        "info": info
    }


# 🔥 NEW: RUN FULL DEMO (THIS SHOWS START → END)
@app.get("/run-demo")
def run_demo():
    logs = []

    obs = env.reset()
    logs.append("START")

    done = False

    while not done:
        task = obs.tasks[0]

        if task.priority == "high":
            action = Action(action_type="complete", task_id=task.id)
        elif task.priority == "medium":
            action = Action(action_type="schedule", task_id=task.id)
        else:
            action = Action(action_type="respond", task_id=task.id)

        obs, reward, done, info = env.step(action)

        logs.append(f"STEP | action={action.action_type} | reward={reward:.2f} | score={info['score']:.2f}")

    logs.append("END")
    logs.append(f"FINAL_SCORE: {info['score']:.2f}")

    return {"logs": logs}