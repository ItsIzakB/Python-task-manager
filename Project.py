import Task
class ProjectClass:

    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.tasks = []
    def addTask(self, task):
        self.tasks.append(task)
    def getProjName(self) -> str:
        return self.name

    def getProjDate(self):
        return self.date

