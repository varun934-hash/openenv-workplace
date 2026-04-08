from pydantic import BaseModel
from typing import List

class Task(BaseModel):
    id: int
    description: str
    priority: str
    status: str
    expected_action: str   # 🔥 REQUIRED

class Observation(BaseModel):
    tasks: List[Task]

class Action(BaseModel):
    action_type: str
    task_id: int

class Reward(BaseModel):
    score: float