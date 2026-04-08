from models import Task

def easy_task():
    return [
        Task(id=1, description="Client asks for refund", priority="high", status="pending", expected_action="complete"),
        Task(id=2, description="Schedule team meeting", priority="medium", status="pending", expected_action="schedule"),
        Task(id=3, description="Reply to customer email", priority="low", status="pending", expected_action="respond"),
        Task(id=4, description="Handle client complaint", priority="high", status="pending", expected_action="complete"),
    ]