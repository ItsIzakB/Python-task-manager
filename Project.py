import Task
class ProjectClass:

    def __init__(self, name):
        self.name = name
        self.tasks = []
    def addTask(self, task):
        self.tasks.append(task)
    def getProjName(self) -> str:
        return self.name
