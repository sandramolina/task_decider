
def task_decider_function(task1, task2):
    # preferred_task = task1.description
    if task1.description == "Wash the Dishes" and task2.description == "Cook Dinner":
        return task1.description

    if task1.description == "Cook Dinner" and task2.description == "Wash the Dishes":
        return task2.description
