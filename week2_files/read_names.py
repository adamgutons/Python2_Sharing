def setFiles():
	# open our names file w/ people names
	file = open('names.txt', 'r')
	# open a file to write our greetings to 
	writeFile = open('greetings.txt', 'w')
	# return the read and write files
	return file, writeFile

def writeGreeting(file, writeFile):
	# for each line (name) in file, strip the newline character 
	for line in file:
		line = line.rstrip()
		# split the name into a list of first and last 
		line = line.split()
		# write to file line[1] index of last name, line[0] index of first name
		writeFile.write('Hello, Dr. %s, or can I call you %s?\n' % (line[1], line[0]))

def main():
	# call on our methods in main
	file, writeFile = setFiles()
	writeGreeting(file, writeFile)

main()









"""
Old code...

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
"""





#for x in range(len(namesList)):
#	for i in range(0,len(namesList),2):
#		print(x, i)