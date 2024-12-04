import self as self

from Project import ProjectClass
class TaskClass():

    def __init__(self, task_name, due_date):
        self.task_name = task_name
        self.due_date = due_date
        self.atrs = []

    def get_info(self):
        print(
            f'task_name: {self.task_name}, '
            f'due_date: {self.due_date} '
              )

    def add_atrs(self, *args):
        self.atrs.append(args)


    def get_info_and_atrs(self,func):
        def wrapper():
            func()
            for i in range(0, len(self.atrs), 1):
                atr = self.atrs[i]



if __name__ == '__main__':
    print("this is task class")
