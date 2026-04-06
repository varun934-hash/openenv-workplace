from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from env import WorkplaceEnv
from models import Action

app = FastAPI()


def choose_action(task):
    desc = task.description.lower()

    if "refund" in desc or "login" in desc:
        return Action(action_type="complete", task_id=task.id)

    elif "meeting" in desc:
        return Action(action_type="schedule", task_id=task.id)

    else:
        return Action(action_type="respond", task_id=task.id)


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h1>✅ Workplace Decision Engine</h1>
    <p>Status: Running</p>
    <a href="/run-demo">▶ Run Demo</a>
    """


@app.get("/run-demo", response_class=HTMLResponse)
def run_demo():
    try:
        env = WorkplaceEnv()
        obs = env.reset()

        logs = ["START"]
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

        return "<br>".join(logs)

    except Exception as e:
        return f"<h3>❌ Error:</h3><pre>{str(e)}</pre>"