from Task import TaskClass
class ToDo_Task(TaskClass):

    def __init__(self, proj_name, date, task_name):

        super().__init__(proj_name, date, task_name)


myTD_task = ToDo_Task("HW", "11/23/2022", 'Calc 1 HW')

myTD_task.getInfo()
