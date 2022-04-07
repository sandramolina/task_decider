def task_decider_function(task1, task2):
    tasks_list = ["Wash the Dishes", "Cook Dinner", "Clean Windows"]

    if task1.description == tasks_list[0] or task2.description == tasks_list[0]:
        if task1.description == tasks_list[1] or task2.description == tasks_list[1]:
            return "Wash the Dishes"
    
    if task1.description == tasks_list[0] or task2.description == tasks_list[0]:
        if task1.description == tasks_list[2] or task2.description == tasks_list[2]:
            return "Clean Windows"
    
    if task1.description == tasks_list[1] or task2.description == tasks_list[1]:
        if task1.description == tasks_list[2] or task2.description == tasks_list[2]:
            return "Cook Dinner"
