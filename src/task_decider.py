
def task_decider_function(task1, task2):

    if task1.description == "Wash the Dishes" or task2.description == "Wash the Dishes":
        if task1.description == "Cook Dinner" or task2.description == "Cook Dinner":
            return "Wash the Dishes"
    
    if task1.description == "Wash the Dishes" or task2.description == "Wash the Dishes":
        if task1.description == "Clean Windows" or task2.description == "Clean Windows":
            return "Clean Windows"
    
    if task1.description == "Cook Dinner" or task2.description == "Cook Dinner":
        if task1.description == "Clean Windows" or task2.description == "Clean Windows":
            return "Cook Dinner"