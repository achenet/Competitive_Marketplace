#lets code something beautiful today. 

class Competitor:
    def __init__(self,project,name):
        self.size = input("How many members are there?:   ")
        self.members = []
        for i in range(size):
            members.append(input("please enter user name:   "))


class Project:
    def __init__(self,name,founder,description,deadline):
        self.name = name
        self.founder = founder
        self.description = description
        self.deadline = deadline
        self.backers = []
        self.competitors = []

    def addBacker(user):
        user.backedProjects.append(self)
        self.backers.append(user)

    def addCompetitor(self):
        name = input("Please enter new competitor team name:   ")
        competitors.append(Competitor(self,name))

class User:

    def __init__(self):
        self.name = input("Please insert new user name:   ")
        self.foundedProjects = []
        self.backedProjects = []

    def backNewProject(self,project):
        project.addBacker(self)

    def foundNewProject(self):
        name = input("Please enter new project name:   ")
        description = input("Please enter project descripition:   ")
        deadline = int(input("Please enter project deadline, in seconds:   "))
        newProject = Project(name,self,description,deadline)


#test script in another file
