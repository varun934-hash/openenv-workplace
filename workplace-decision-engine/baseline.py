from env import WorkplaceEnv
from models import Action
import random

def simple_agent(observation):
    """
    Simple rule-based agent:
    - Completes high priority tasks first
    - Then medium
    - Then low
    """

    tasks = observation.tasks

    # Sort by priority
    priority_order = {"high": 1, "medium": 2, "low": 3}
    tasks_sorted = sorted(tasks, key=lambda x: priority_order[x.priority])

    for task in tasks_sorted:
        if task.status != "completed":
            return Action(action_type="complete", task_id=task.id)

    return Action(action_type="complete", task_id=tasks[0].id)


def run_episode():
    env = WorkplaceEnv()
    obs = env.reset()

    total_reward = 0

    while True:
        action = simple_agent(obs)
        obs, reward, done, info = env.step(action)

        total_reward += reward

        if done:
            print("Final Score:", info.get("score"))
            print("Total Reward:", total_reward)
            break


if __name__ == "__main__":
    run_episode()