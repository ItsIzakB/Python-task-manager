import self as self

from Project import ProjectClass
class Task():

    def __init__(self, task_name, due_date):
        self.task_name = task_name
        self.due_date = due_date

    def get_info(self):
        print(
            f'task_name: {self.task_name},'
            f'due_date: {self.due_date}, '
              )

    def task_atr(self, *args):
        taskAtrs = args

        return taskAtrs


print("this is task class")
