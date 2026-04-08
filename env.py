from tasks import easy_task
from models import Observation


class WorkplaceEnv:
    def __init__(self):
        self.tasks = []
        self.task_rewards = {}

    def reset(self):
        self.tasks = easy_task()
        self.task_rewards = {}
        return Observation(tasks=self.tasks)

    def step(self, action):
        reward = 0.2

        for task in self.tasks:
            if task.id == action.task_id and task.status == "pending":

                # 🔥 GRADING LOGIC (DETECTABLE)
                if action.action_type == task.expected_action:
                    reward = 0.8
                else:
                    reward = 0.4

                self.task_rewards[task.id] = reward
                task.status = "completed"
                break

        done = all(task.status == "completed" for task in self.tasks)

        # 🔥 FINAL SCORE FROM ALL TASKS
        if len(self.task_rewards) >= 3:
            final_score = sum(self.task_rewards.values()) / len(self.task_rewards)
        else:
            final_score = 0.5

        # enforce strict range
        if final_score <= 0:
            final_score = 0.3
        elif final_score >= 1:
            final_score = 0.85

        return Observation(tasks=self.tasks), reward, done, {"score": final_score}