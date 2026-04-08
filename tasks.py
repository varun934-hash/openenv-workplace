from models import Task

def easy_task():
    return [
        Task(
            id=1,
            description="Client asks for refund",
            priority="high",
            status="pending"
        ),
        Task(
            id=2,
            description="Schedule team meeting",
            priority="medium",
            status="pending"
        ),
        Task(
            id=3,
            description="Reply to customer email",
            priority="low",
            status="pending"
        ),
        Task(
            id=4,
            description="Handle client complaint",
            priority="high",
            status="pending"
        ),
    ]