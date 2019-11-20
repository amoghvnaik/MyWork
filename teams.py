file = open('teams.txt', 'w')
teams = "Manchester United" + "\n" + "Manchester City" + "\n" + "Liverpool" + "\n" + "Norwich" +"\n" + "West Ham"
file.write(teams)

file = open('teams.txt', 'r')
print(file.readline())
print(file.readline())

file.close()
