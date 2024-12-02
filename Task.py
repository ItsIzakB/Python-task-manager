import self as self

from Project import ProjectClass
class Task(ProjectClass):

    def __init__(self, proj_name, date, task_name):
        super().__init__(proj_name, date)
        self.task_name = task_name

    def getInfo(self):
        print(f'ProjName: {self.name}, '
              f'Proj_date: {self.date}, '
              f'task_name: {self.task_name}')


myT = Task('Proj A', '11', 'T1')

print(myT.getProjName())
print(myT.getProjDate())
myT.getInfo()
