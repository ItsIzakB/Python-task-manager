import self as self

import Project
class Task(Project):

    def __init__(self, proj_name, date, task_name):
        super().__init__(proj_name, date)
        self.name = task_name

    def getInfo(self):
        print(f'ProjName: {self.proj_name}, '
              f'Proj_date: {self.date}, '
              f'task_name: {self.task_name}')


myT = Task('Proj A', '11', 'T1')

myT.get
