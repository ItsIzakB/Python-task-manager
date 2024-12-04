import self as self

from Project import ProjectClass
class TaskClass():

    def __init__(self, task_name, due_date):
        self.task_name = task_name
        self.due_date = due_date
        self.atr = []

    def get_info(self):
        print(
            f'task_name: {self.task_name},'
            f'due_date: {self.due_date}, '
              )

    def add_atrs(self, *args):
        self.atr.append(args)

if '__name__' == '__main__':
    print("this is task class")
