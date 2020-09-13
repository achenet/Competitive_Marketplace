import firstdraft

UserList = []
ProjectList = []

UserList.append(User())
UserList.append(User())
for i in UserList:
    print(i.name)

ProjectList.append(UserList[0].foundNewProject())
UserList[1].backNewProject(ProjectList[0])
ProjectList[0].addCompetitor()
for i in ProjectList:
    print(i.name)
    print(i.description)
    print(i.backers)
    print(i.competitors)
    print(i.deadline)

