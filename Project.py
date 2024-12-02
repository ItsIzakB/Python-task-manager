class ProjectClass:

    def __init__(self, name, date):
        self.name = name
        self.date = date

    def getProjName(self) -> str:
        return self.name

    def getProjDate(self):
        return self.date

