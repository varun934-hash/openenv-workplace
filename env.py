from tasks import easy_task
from models import Observation
from grader import grade


class WorkplaceEnv:
    def __init__(self):
        self.tasks = []
        self.task_scores = {}   # 🔥 track each task grading

    # -------------------------------
    # RESET
    # -------------------------------
    def reset(self):
        self.tasks = easy_task()
        self.task_scores = {}   # reset scores
        return self._get_observation()

    # -------------------------------
    # STEP (FIXED PROPERLY)
    # -------------------------------
    def step(self, action):
        reward = 0.1

        for task in self.tasks:
            if task.id == action.task_id and task.status == "pending":

                # 🔥 grade THIS specific task
                reward = grade(task, action)

                # store score per task
                self.task_scores[task.id] = reward

                task.status = "completed"
                break

        done = all(task.status == "completed" for task in self.tasks)

        # 🔥 FINAL SCORE FROM ALL TASKS
        if len(self.task_scores) == 0:
            final_score = 0.3
        else:
            final_score = sum(self.task_scores.values()) / len(self.tasks)

        # ensure strictly between (0,1)
        if final_score <= 0:
            final_score = 0.3
        elif final_score >= 1:
            final_score = 0.85

        return self._get_observation(), reward, done, {"score": final_score}

    # -------------------------------
    def _get_observation(self):
        return Observation(tasks=self.tasks)