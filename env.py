from tasks import easy_task
from models import Observation
from grader import grade


class WorkplaceEnv:
    def __init__(self):
        self.tasks = []

    # -------------------------------
    # RESET ENVIRONMENT
    # -------------------------------
    def reset(self):
        self.tasks = easy_task()
        return self._get_observation()

    # -------------------------------
    # STEP FUNCTION (WITH GRADER)
    # -------------------------------
    def step(self, action):
        reward = 0.1  # default small reward

        for task in self.tasks:
            if task.id == action.task_id and task.status == "pending":

                # 🔥 USE GRADER (VERY IMPORTANT)
                reward = grade(task, action)

                # mark task completed
                task.status = "completed"
                break

        # check if all tasks completed
        done = all(task.status == "completed" for task in self.tasks)

        # 🔥 CALCULATE SCORE BASED ON ALL TASKS
        scores = []
        for task in self.tasks:
            if task.status == "completed":
                # use same action logic to evaluate
                scores.append(grade(task, action))

        # safe score calculation
        if len(scores) == 0:
            final_score = 0.3
        else:
            final_score = sum(scores) / len(scores)

        # 🔥 ENSURE SCORE STRICTLY BETWEEN (0,1)
        if final_score <= 0:
            final_score = 0.3
        elif final_score >= 1:
            final_score = 0.85

        return self._get_observation(), reward, done, {"score": final_score}

    # -------------------------------
    # OBSERVATION
    # -------------------------------
    def _get_observation(self):
        return Observation(tasks=self.tasks)