from fastapi import FastAPI
from pydantic import BaseModel
from env import WorkplaceEnv
from models import Action

app = FastAPI()

# Global env
env = WorkplaceEnv()


# -------------------------------
# Helper function
# -------------------------------
def choose_action(task):
    desc = task.description.lower()

    if "refund" in desc or "complaint" in desc:
        return Action(action_type="complete", task_id=task.id)

    elif "meeting" in desc:
        return Action(action_type="schedule", task_id=task.id)

    else:
        return Action(action_type="respond", task_id=task.id)


# -------------------------------
# ROOT
# -------------------------------
@app.get("/")
def root():
    return {"status": "running"}


# -------------------------------
# RESET (IMPORTANT)
# -------------------------------
@app.post("/reset")
def reset():
    obs = env.reset()
    return {
        "tasks": [task.dict() for task in obs.tasks]
    }


# -------------------------------
# STEP (IMPORTANT)
# -------------------------------
class StepRequest(BaseModel):
    action_type: str
    task_id: int


@app.post("/step")
def step(req: StepRequest):
    action = Action(action_type=req.action_type, task_id=req.task_id)

    obs, reward, done, info = env.step(action)

    return {
        "tasks": [task.dict() for task in obs.tasks],
        "reward": reward,
        "done": done,
        "score": info["score"]
    }


# -------------------------------
# RUN DEMO (FOR SCALER)
# -------------------------------
@app.get("/run-demo")
def run_demo():
    obs = env.reset()

    step_count = 0
    task_name = "workplace_decision"

    logs = []

    # START
    print(f"[START] task={task_name}", flush=True)
    logs.append("[START]")

    done = False

    while not done:
        for task in obs.tasks:
            if task.status == "completed":
                continue

            action = choose_action(task)

            obs, reward, done, info = env.step(action)

            step_count += 1

            step_log = f"[STEP] step={step_count} reward={reward:.2f}"
            print(step_log, flush=True)
            logs.append(step_log)

            if done:
                break

    final_score = info["score"]

    end_log = f"[END] task={task_name} score={final_score:.2f} steps={step_count}"
    print(end_log, flush=True)
    logs.append(end_log)

    return {"logs": logs}