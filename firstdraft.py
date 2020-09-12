#lets code something beautiful today. 

class Project:
    def __init__(self,name,founder,description,deadline):
        self.name = name
        self.founder = founder
        self.description = description
        self.deadline = deadline
        self.backers = []
        self.


class User:

    def __init__(self):
        self.name = input("Please insert new user name")
        self.foundedProjects = []
        self.backedProjects = []

    def backNewProject(self,project):
        project.addNewBacker(self)

    def foundNewProject(self):
        name = input("Please enter new project name")
        description = input("Please enter project descripition")
        deadline = int(input("Please enter project deadline, in seconds"))
        newProject = Project(name,self,description,deadline)

