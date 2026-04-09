from tasks import easy_task
from models import Observation, Reward


class WorkplaceEnv:
    def __init__(self):
        self.tasks = []
        self.task_scores = {}

    def reset(self):
        self.tasks = easy_task()
        self.task_scores = {}
        return Observation(tasks=self.tasks)

    def step(self, action):
        score = 0.2

        for task in self.tasks:
            if task.id == action.task_id and task.status == "pending":

                # ✅ GRADING LOGIC (VISIBLE)
                if action.action_type == task.expected_action:
                    score = 0.8
                else:
                    score = 0.4

                # ✅ STORE PER TASK SCORE
                self.task_scores[task.id] = score

                task.status = "completed"
                break

        done = all(task.status == "completed" for task in self.tasks)

        # ✅ FINAL SCORE FROM MULTIPLE TASKS
        if len(self.task_scores) >= 3:
            final_score = sum(self.task_scores.values()) / len(self.task_scores)
        else:
            final_score = 0.5

        # enforce strict (0,1)
        if final_score <= 0:
            final_score = 0.3
        elif final_score >= 1:
            final_score = 0.85

        # 🔥 IMPORTANT: USE Reward OBJECT
        reward_obj = Reward(score=score)

        return (
            Observation(tasks=self.tasks),
            reward_obj.score,   # step reward
            done,
            {"score": final_score}
        )