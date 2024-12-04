import self as self

from Project import ProjectClass
class Task():

    def __init__(self, task_name, date, task_name):
        self.name = task_name
        self.date = date
        self.task_name = task_name

    def getInfo(self):
        print(f'Task_name: {self.name}, '
              f'Proj_date: {self.date}, '
              f'task_name: {self.task_name}')

    def taskAtr(self, *args):
        taskAtrs = args

        return taskAtrs
