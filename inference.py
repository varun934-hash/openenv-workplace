import os
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

from env import WorkplaceEnv
from models import Action

app = FastAPI()

# Global environment
env = WorkplaceEnv()

# -------------------------------
# LLM CLIENT (SAFE INIT)
# -------------------------------
client = None

if os.environ.get("API_KEY") and os.environ.get("API_BASE_URL"):
    client = OpenAI(
        base_url=os.environ.get("API_BASE_URL"),
        api_key=os.environ.get("API_KEY"),
    )


# -------------------------------
# ACTION USING LLM + FALLBACK
# -------------------------------
def choose_action(task):
    # 🔥 Try LLM (Scaler environment)
    if client:
        prompt = f"""
        You are a workplace assistant.

        Task:
        {task.description}

        Choose one action:
        - complete
        - schedule
        - respond

        Return only the action.
        """

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
            )

            action_text = response.choices[0].message.content.strip().lower()

            if "complete" in action_text:
                return Action(action_type="complete", task_id=task.id)
            elif "schedule" in action_text:
                return Action(action_type="schedule", task_id=task.id)
            else:
                return Action(action_type="respond", task_id=task.id)

        except Exception:
            pass  # fallback below

    # 🔥 LOCAL FALLBACK (IMPORTANT)
    desc = task.description.lower()

    if "refund" in desc or "complaint" in desc:
        return Action(action_type="complete", task_id=task.id)
    elif "meeting" in desc:
        return Action(action_type="schedule", task_id=task.id)
    else:
        return Action(action_type="respond", task_id=task.id)


# -------------------------------
# CORE SIMULATION (PRINTS LOGS)
# -------------------------------
def run_simulation(print_logs=True):
    obs = env.reset()

    step_count = 0
    task_name = "workplace_decision"

    logs = []

    # START
    start_log = f"[START] task={task_name}"
    if print_logs:
        print(start_log, flush=True)
    logs.append(start_log)

    done = False

    while not done:
        for task in obs.tasks:
            if task.status == "completed":
                continue

            action = choose_action(task)

            obs, reward, done, info = env.step(action)

            step_count += 1

            step_log = f"[STEP] step={step_count} reward={reward:.2f}"
            if print_logs:
                print(step_log, flush=True)
            logs.append(step_log)

            if done:
                break

    final_score = info["score"]

    end_log = f"[END] task={task_name} score={final_score:.2f} steps={step_count}"
    if print_logs:
        print(end_log, flush=True)
    logs.append(end_log)

    return logs


# -------------------------------
# API ENDPOINTS (PHASE 1)
# -------------------------------
@app.get("/")
def root():
    return {"status": "running"}


@app.post("/reset")
def reset():
    obs = env.reset()
    return {"tasks": [task.dict() for task in obs.tasks]}


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


@app.get("/run-demo")
def run_demo():
    logs = run_simulation(print_logs=True)
    return {"logs": logs}


# -------------------------------
# 🔥 REQUIRED FOR SCALER (CRITICAL)
# -------------------------------
if __name__ == "__main__":
    run_simulation(print_logs=True)