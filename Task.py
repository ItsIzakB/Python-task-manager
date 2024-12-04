import self as self

from Project import ProjectClass
class Task():

    def __init__(self, proj_name, date, task_name):
        proj = ProjectClass(proj_name)
        self.date = date
        self.task_name = task_name

    def getInfo(self):
        print(f'ProjName: {self.name}, '
              f'Proj_date: {self.date}, '
              f'task_name: {self.task_name}')

    def taskAtr(self, *args):
        taskAtrs = args

        return taskAtrs


# myT = Task('Proj A', '11', 'T1')
#
# print(myT.getProjName())
# print(myT.getProjDate())
# myT.getInfo()
#
# print(myT.taskAtr('difficult', 'urgent'))
