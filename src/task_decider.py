# def task_decider_function(task1, task2):
#     tasks_list = ["Wash the Dishes", "Cook Dinner", "Clean Windows"]

#     if task1.description == tasks_list[0] or task2.description == tasks_list[0]:
#         if task1.description == tasks_list[1] or task2.description == tasks_list[1]:
#             return "Wash the Dishes"
    
#     if task1.description == tasks_list[0] or task2.description == tasks_list[0]:
#         if task1.description == tasks_list[2] or task2.description == tasks_list[2]:
#             return "Clean Windows"
    
#     if task1.description == tasks_list[1] or task2.description == tasks_list[1]:
#         if task1.description == tasks_list[2] or task2.description == tasks_list[2]:
#             return "Cook Dinner"

def task_decider_function(task1, task2):
    tasks_list = ["Wash the Dishes", "Cook Dinner", "Clean Windows", ""]
    index_list = []
    for index, task in enumerate(tasks_list):
        if task1.description == task:
            index_list.append(index)
    for index, task in enumerate(tasks_list):
        if task2.description == task:
            index_list.append(index)
    
    sorted(index_list)
    difference = index_list[1] - index_list[0]
    if difference % 2 == 0:
        return tasks_list[index_list[1]]
    else:
        return tasks_list[index_list[0]]


