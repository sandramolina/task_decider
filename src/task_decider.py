def task_decider_function(task1, task2):
    tasks_list = ["Wash the Dishes", "Cook Dinner", "Do Ironing", "Wash Clothes", "Clean Windows"]
    index_list = []
    for index, task in enumerate(tasks_list):
        if task1.description == task:
            index_list.append(index)
    for index, task in enumerate(tasks_list):
        if task2.description == task:
            index_list.append(index)
    
    index_list = sorted(index_list)
    difference = index_list[1] - index_list[0]
    if difference % 2 == 0:
        return tasks_list[index_list[1]]
    else:
        return tasks_list[index_list[0]]


