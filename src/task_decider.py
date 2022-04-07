
def task_decider_function(task1, task2):

    if task1.description == "Wash the Dishes" or task2.description == "Wash the Dishes":
        if task1.description == "Cook Dinner" or task2.description == "Cook Dinner":
            return "Wash the Dishes"
    
