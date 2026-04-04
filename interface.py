import os
from env import WorkplaceEnv
from models import Action

# ✅ Required environment variables
API_BASE_URL = os.getenv("API_BASE_URL", "default")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
HF_TOKEN = os.getenv("HF_TOKEN")


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


def run():
    env = WorkplaceEnv()
    obs = env.reset()

    print("START")

    done = False

    while not done:
        for task in obs.tasks:
            if task.status == "completed":
                continue

            action = choose_action(task)

            obs, reward, done, info = env.step(action)

            print(f"STEP | action={action.action_type} | reward={reward:.2f} | score={info['score']:.2f}")

            if done:
                break

    print("END")
    print(f"FINAL_SCORE: {info['score']:.2f}")


if __name__ == "__main__":
    run()