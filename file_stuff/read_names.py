file = open('names.txt', 'r')
writeFile = open('greetings.txt', 'w')
namesList = []
firstNames = []
lastNames = []

for line in file:
	line = line.rstrip()
	namesList.append(line.split())
	print(namesList)

for x in range(len(namesList)):
	for i in range(len(namesList[x])-1):
		firstNames.append(namesList[x][i])
		print(firstNames)

for x in range(len(namesList)):
	for i in range(1,len(namesList[x]),2):
		lastNames.append(namesList[x][i])
		print(lastNames)

for i in range(len(firstNames)):
	writeFile.write('Hello, Dr. %s, or can I call you %s?\n' % (lastNames[i], firstNames[i]))






#for x in range(len(namesList)):
#	for i in range(0,len(namesList),2):
#		print(x, i)