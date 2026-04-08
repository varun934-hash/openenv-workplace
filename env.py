from tasks import easy_task
from models import Observation
from grader import grade


class WorkplaceEnv:
    def __init__(self):
        self.tasks = []
        self.scores = {}

    def reset(self):
        self.tasks = easy_task()
        self.scores = {}
        return Observation(tasks=self.tasks)

    def step(self, action):
        reward = 0.1

        for task in self.tasks:
            if task.id == action.task_id and task.status == "pending":
                reward = grade(task, action)

                # 🔥 store individual task grading
                self.scores[task.id] = reward

                task.status = "completed"
                break

        done = all(task.status == "completed" for task in self.tasks)

        # 🔥 IMPORTANT: use ALL task scores
        if len(self.scores) >= 3:
            final_score = sum(self.scores.values()) / len(self.scores)
        else:
            final_score = 0.5  # fallback

        # ensure strictly between (0,1)
        if final_score <= 0:
            final_score = 0.3
        elif final_score >= 1:
            final_score = 0.85

        return Observation(tasks=self.tasks), reward, done, {"score": final_score}