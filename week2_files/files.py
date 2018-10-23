newFile = open('file.txt', 'w')

ten = 10
for x in range(ten):
	for i in range(ten):
		newFile.write(str(i))
	ten -= 1
	newFile.write('\n')	

newFile.flush()
newFile.close()		
