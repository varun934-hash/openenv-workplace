from fastapi import FastAPI
from env import WorkplaceEnv
from models import Action

# ✅ Enable docs explicitly
app = FastAPI(
    title="Workplace Decision Engine",
    description="AI-powered task prioritization system",
    version="1.0",
    docs_url="/docs",          # IMPORTANT
    redoc_url="/redoc",        # OPTIONAL
    openapi_url="/openapi.json"
)

env = WorkplaceEnv()


# ✅ HOME
@app.get("/")
def home():
    return {"status": "running"}


# ✅ RESET
@app.post("/reset")
def reset():
    obs = env.reset()
    return obs.model_dump()


# ✅ STEP
@app.post("/step")
def step(action: Action):
    obs, reward, done, info = env.step(action)
    return {
        "observation": obs.model_dump(),
        "reward": reward,
        "done": done,
        "info": info
    }


# ✅ DEMO
@app.get("/run-demo")
def run_demo():
    logs = []

    obs = env.reset()
    logs.append("START")

    done = False

    while not done:
        if not obs.tasks:
            break

        task = obs.tasks[0]

        if task.priority == "high":
            action = Action(action_type="complete", task_id=task.id)
        elif task.priority == "medium":
            action = Action(action_type="schedule", task_id=task.id)
        else:
            action = Action(action_type="respond", task_id=task.id)

        obs, reward, done, info = env.step(action)

        logs.append(
            f"STEP | action={action.action_type} | reward={reward:.2f} | score={info.get('score', 0):.2f}"
        )

    logs.append("END")
    logs.append(f"FINAL_SCORE: {info.get('score', 0):.2f}")

    return {"logs": logs}