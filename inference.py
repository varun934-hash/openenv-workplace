from fastapi import FastAPI
from env import WorkplaceEnv
from models import Action

app = FastAPI()


def choose_action(task):
    desc = task.description.lower()

    if "login" in desc:
        return Action(action_type="complete", task_id=task.id)

    elif "refund" in desc:
        return Action(action_type="complete", task_id=task.id)

    elif "meeting" in desc:
        return Action(action_type="schedule", task_id=task.id)

    else:
        return Action(action_type="respond", task_id=task.id)


@app.get("/")
def home():
    return {"message": "Workplace Decision Engine Running ✅"}


@app.get("/run-demo")
def run_demo():
    env = WorkplaceEnv()
    obs = env.reset()

    logs = []
    logs.append("START")

    done = False

    while not done:
        for task in obs.tasks:
            if task.status == "completed":
                continue

            action = choose_action(task)

            obs, reward, done, info = env.step(action)

            logs.append(
                f"STEP | action={action.action_type} | reward={reward:.2f} | score={info['score']:.2f}"
            )

            if done:
                break

    logs.append("END")
    logs.append(f"FINAL_SCORE: {info['score']:.2f}")

    return {"logs": logs}