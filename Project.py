class ProjectClass:

    def __init__(self, name):
        self.name = name
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
    def get_proj_name(self) -> str:
        return self.name
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if (self.index>= len(self.tasks)):
            return StopIteration
        else:
            task = self.tasks[self.index]
            self.index+=1
            return task



if __name__ == '__main__':
    print("this is project class")


