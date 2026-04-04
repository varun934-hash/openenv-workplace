<<<<<<< HEAD
from models import Task

# EASY TASK
def easy_task():
    return [
        Task(id=1, description="Client asks for refund", priority="high", status="pending")
    ]

# MEDIUM TASK
def medium_task():
    return [
        Task(id=1, description="Client refund request", priority="high", status="pending"),
        Task(id=2, description="Schedule meeting", priority="medium", status="pending")
    ]

# HARD TASK
def hard_task():
    return [
        Task(id=1, description="Urgent client complaint", priority="high", status="pending"),
        Task(id=2, description="Prepare report", priority="medium", status="pending"),
        Task(id=3, description="Team lunch planning", priority="low", status="pending"),
=======
from models import Task

# EASY TASK
def easy_task():
    return [
        Task(id=1, description="Client asks for refund", priority="high", status="pending")
    ]

# MEDIUM TASK
def medium_task():
    return [
        Task(id=1, description="Client refund request", priority="high", status="pending"),
        Task(id=2, description="Schedule meeting", priority="medium", status="pending")
    ]

# HARD TASK
def hard_task():
    return [
        Task(id=1, description="Urgent client complaint", priority="high", status="pending"),
        Task(id=2, description="Prepare report", priority="medium", status="pending"),
        Task(id=3, description="Team lunch planning", priority="low", status="pending"),
>>>>>>> 0c94d1aa3ad327c92e2fbd0af7b279095d94b96a
    ]