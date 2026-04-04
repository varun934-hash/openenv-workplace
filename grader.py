<<<<<<< HEAD
def grade_tasks(tasks):
    total = len(tasks)
    completed = sum(1 for t in tasks if t.status == "completed")

    # score between 0.0 to 1.0
=======
def grade_tasks(tasks):
    total = len(tasks)
    completed = sum(1 for t in tasks if t.status == "completed")

    # score between 0.0 to 1.0
>>>>>>> 0c94d1aa3ad327c92e2fbd0af7b279095d94b96a
    return completed / total if total > 0 else 0.0