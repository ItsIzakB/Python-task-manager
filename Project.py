class Project:

    def _init_(self, name, date):
        self.name = name
        self.date = date

    def getName(self) -> str:
        return self.name


myProj = Project()
