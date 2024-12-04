import self as self

from Project import ProjectClass
class Task():

    def __init__(self, due_date, task_name):
        self.due_date = due_date
        self.task_name = task_name

    def getInfo(self):
        print(
              f'due_date: {self.due_date}, '
              f'task_name: {self.task_name}')

    def taskAtr(self, *args):
        taskAtrs = args

        return taskAtrs
