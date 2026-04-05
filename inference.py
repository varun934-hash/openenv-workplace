from models import Task, Action

# ✅ STATIC TASKS (guaranteed working)
def get_tasks():
    return [
        Task(id=1, description="Login issue", priority="high", status="pending"),
        Task(id=2, description="Schedule meeting", priority="medium", status="pending"),
        Task(id=3, description="Lunch plan", priority="low", status="pending"),
    ]


def choose_action(task):
    if task.priority == "high":
        return "complete"
    elif task.priority == "medium":
        return "schedule"
    else:
        return "respond"


# ✅ FINAL DEMO FUNCTION
def run_demo():
    tasks = get_tasks()

    logs = []
    logs.append("START")

    score = 0

    for task in tasks:
        action = choose_action(task)

        # simple reward logic
        if task.priority == "high" and action == "complete":
            reward = 1.0
        elif task.priority == "medium" and action == "schedule":
            reward = 0.5
        else:
            reward = 0.2

        score += reward

        logs.append(
            f"STEP | action={action} | reward={reward:.2f} | score={score:.2f}"
        )

    logs.append("END")
    logs.append(f"FINAL_SCORE: {score:.2f}")

    return {"logs": logs}


# ✅ LOCAL RUN
if __name__ == "__main__":
    result = run_demo()

    for line in result["logs"]:
        print(line)