from tasks import easy_task
from models import Observation


class WorkplaceEnv:
    def __init__(self):
        self.tasks = []
        self.task_scores = {}

    def reset(self):
        self.tasks = easy_task()
        self.task_scores = {}
        return Observation(tasks=self.tasks)

    def step(self, action):
        reward = 0.2

        for task in self.tasks:
            if task.id == action.task_id and task.status == "pending":

                # 🔥 EXPLICIT GRADING PER TASK
                if action.action_type == task.expected_action:
                    reward = 0.8
                else:
                    reward = 0.4

                # 🔥 STORE SCORE FOR THIS TASK
                self.task_scores[task.id] = reward

                task.status = "completed"
                break

        done = all(task.status == "completed" for task in self.tasks)

        # 🔥 VERY IMPORTANT: USE ALL TASK SCORES
        total_tasks = len(self.tasks)
        graded_tasks = len(self.task_scores)

        if graded_tasks >= 3:
            final_score = sum(self.task_scores.values()) / total_tasks
        else:
            final_score = 0.5

        # ensure strict range
        if final_score <= 0:
            final_score = 0.3
        elif final_score >= 1:
            final_score = 0.85

        return Observation(tasks=self.tasks), reward, done, {"score": final_score}