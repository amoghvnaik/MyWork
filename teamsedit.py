from teams import teams

file = open('teams.txt', 'w')
firstline = 'This is the first line' + '\n'
file.write(firstline)
file.write(teams)

file.close()
          
