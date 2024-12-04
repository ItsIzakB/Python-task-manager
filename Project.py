class ProjectClass:

    def __init__(self, name):
        self.name = name
        self.tasks = []
    def addTask(self, task):
        self.tasks.append(task)
    def getProjName(self) -> str:
        return self.name
    def __iter__(self):
        return self.tasks

    def __next__(self):




print("this is project class")


