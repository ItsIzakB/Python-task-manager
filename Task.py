import self as self

from Project import ProjectClass

def get_info_and_atrs(func):
    def wrapper(self, *args, **kwargs):
        func(self, *args, **kwargs)
        if self.atrs:
            print(self.atrs, end=' ')
    return wrapper
    
class TaskClass():

    def __init__(self, task_name, due_date):
        self.task_name = task_name
        self.due_date = due_date
        self.atrs = []

    @get_info_and_atrs
    def get_info(self):
        print(
            f'task_name: {self.task_name}, '
            f'due_date: {self.due_date} '
              )

    def add_atrs(self, *args):
        self.atrs.append(args)

if __name__ == '__main__':
    print("this is task class")
