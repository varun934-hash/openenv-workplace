from pydantic import BaseModel
from typing import List

# Task model
class Task(BaseModel):
    id: int
    description: str
    priority: str  # low, medium, high
    status: str  # pending, completed


# Observation model
class Observation(BaseModel):
    tasks: List[Task]


# Action model
class Action(BaseModel):
    action_type: str  # respond, escalate, schedule, complete
    task_id: int


# Reward model
class Reward(BaseModel):
    score: float