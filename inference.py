from env import WorkplaceEnv
from models import Action


def choose_action(task):
    desc = task.description.lower()

    if "refund" in desc or "complaint" in desc:
        return Action(action_type="complete", task_id=task.id)

    elif "meeting" in desc:
        return Action(action_type="schedule", task_id=task.id)

    else:
        return Action(action_type="respond", task_id=task.id)


def run():
    env = WorkplaceEnv()
    obs = env.reset()

    step_count = 0
    task_name = "workplace_decision"

    # ✅ START BLOCK
    print(f"[START] task={task_name}", flush=True)

    done = False

    while not done:
        for task in obs.tasks:
            if task.status == "completed":
                continue

            action = choose_action(task)

            obs, reward, done, info = env.step(action)

            step_count += 1

            # ✅ STEP BLOCK
            print(
                f"[STEP] step={step_count} reward={reward:.2f}",
                flush=True
            )

            if done:
                break

    final_score = info["score"]

    # ✅ END BLOCK
    print(
        f"[END] task={task_name} score={final_score:.2f} steps={step_count}",
        flush=True
    )


if __name__ == "__main__":
    run()