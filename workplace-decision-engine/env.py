from models import Task, Observation, Action
from tasks import easy_task, medium_task, hard_task
from grader import grade_tasks
import random


class WorkplaceEnv:
    def __init__(self):
        self.tasks = []
        self.step_count = 0
        self.max_steps = 10

    # RESET: start new episode
    def reset(self):
        task_type = random.choice(["easy", "medium", "hard"])

        if task_type == "easy":
            self.tasks = easy_task()
        elif task_type == "medium":
            self.tasks = medium_task()
        else:
            self.tasks = hard_task()

        self.step_count = 0
        return self._get_observation()

    # STATE: return full internal state
    def state(self):
        return self.tasks

    # OBSERVATION: what AI sees
    def _get_observation(self):
        return Observation(tasks=self.tasks)

    # STEP: core logic
    def step(self, action: Action):
        reward = 0.0
        done = False
        info = {}

        self.step_count += 1

        # Find task
        task = next((t for t in self.tasks if t.id == action.task_id), None)

        if not task:
            reward -= 0.5  # invalid task
        else:
            # Action logic
            if action.action_type == "complete":
                if task.priority == "high":
                    reward += 1.0
                elif task.priority == "medium":
                    reward += 0.5
                else:
                    reward += 0.2

                task.status = "completed"

            elif action.action_type == "respond":
                reward += 0.3

            elif action.action_type == "escalate":
                if task.priority == "high":
                    reward += 0.5
                else:
                    reward -= 0.2

            elif action.action_type == "schedule":
                if task.priority == "medium":
                    reward += 0.4
                else:
                    reward -= 0.2

            else:
                reward -= 0.3  # invalid action

        # Penalty for ignoring high priority tasks
        for t in self.tasks:
            if t.priority == "high" and t.status != "completed":
                reward -= 0.1

        # Check if all tasks completed
        if all(t.status == "completed" for t in self.tasks):
            done = True

        # Max steps reached
        if self.step_count >= self.max_steps:
            done = True

        # Final score (0.0 to 1.0)
        info["score"] = grade_tasks(self.tasks)

        return self._get_observation(), reward, done, info