
from typing import List
from pydantic import BaseModel
from tasks import Task, easy_task   # ✅ import Task from tasks.py


class Observation(BaseModel):
    tasks: List[Task]


class Action(BaseModel):
    action_type: str
    task_id: int


class WorkplaceEnv:
    def __init__(self):
        self.tasks: List[Task] = []
        self.step_count = 0
        self.max_steps = 10

    def reset(self):
        self.tasks = easy_task()
        self.step_count = 0
        return self._get_observation()

    def step(self, action: Action):
        reward = 0.0

        for task in self.tasks:
            if task.id == action.task_id and task.status != "completed":

                if action.action_type == "complete":
                    task.status = "completed"
                    reward = 1.0 if task.priority == "high" else 0.5

                elif action.action_type == "schedule":
                    reward = 0.5 if task.priority == "medium" else -0.4

                elif action.action_type == "respond":
                    reward = 0.2 if task.priority == "low" else -0.2

                elif action.action_type == "escalate":
                    reward = 0.3

        self.step_count += 1

        done = all(t.status == "completed" for t in self.tasks) or self.step_count >= self.max_steps

        score = sum(1 for t in self.tasks if t.status == "completed") / len(self.tasks)

        return self._get_observation(), reward, done, {"score": score}

    def _get_observation(self):
        return Observation(tasks=self.tasks)

def reset(self):
    from email_reader import fetch_unread_emails
    from email_to_task import emails_to_tasks, easy_task
    import os

    print("\n--- DEBUG START ---")

    try:
        # 🔥 HF SAFE MODE (no email in cloud)
        if os.getenv("HF_SPACE"):
            emails = []
        else:
            emails = fetch_unread_emails()

        print("Fetched Emails:", emails)

        tasks = emails_to_tasks(emails)
        print("Converted Tasks:", tasks)

        if tasks:
            self.tasks = tasks
            print("Using EMAIL TASKS ✅")
        else:
            self.tasks = easy_task()
            print("Using DEFAULT TASKS ❌")

    except Exception as e:
        print("Email Error:", e)
        self.tasks = easy_task()
        print("Fallback to DEFAULT TASKS ❌")

    print("--- DEBUG END ---\n")

    self.step_count = 0
    return self._get_observation()
 
