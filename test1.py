import firstdraft as F

UserList = []
ProjectList = []

UserList.append(F.User())
UserList.append(F.User())
UserList[0].foundNewProject()

for u in UserList:
    print(u.name)
    print(u.foundedProjects)
    for p in u.foundedProjects:
        ProjectList.append(p)


print("full list of projects")
print(ProjectList)

#ProjectList[0].__Project__addCompetitor()
#for i in ProjectList:
#    print(i.name)
#    print(i.description)
#    print(i.backers)
#    print(i.competitors)
#    print(i.deadline)

