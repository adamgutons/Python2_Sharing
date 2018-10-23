import os

#you can set whatever path in the concactonated part of the string
path = os.environ['HOME'] + '/weebly'
#path = "/home/techred3/weebly"

rootList = []
dirList = []
filesList = []
finalDict = {}
for (root, dirnames, files) in os.walk(path, topdown=True): # for all roots, directories, and files in the path
	rootList.append(root) # append the root strings to rootList
	if dirnames == []: # if a path contains an empty directory, append 'no dir foudn'
		dirList.append('no dir found')
	dirList.append(dirnames) # append directories to dirList

for d in dirList: # for each directory in directory list, if no directories (empty list []) remove the empty list
	if d == []:
		dirList.remove(d)

for i in range(len(rootList)):	# iterate over length of root list to add to empty dict, key is root value is directories inside of it
	finalDict[rootList[i]] = dirList[i] 

print(finalDict)
print(finalDict[path])
print(finalDict[path][0])

print(dirList)
#for key in sorted(finalDict):
#	print(key, finalDict[key])



	#for i in range(len(rootList)):
	#	finalDict[rootList[i]] = dirnames[i]

"""
for i in range(len(dirList)):
	for (root, dirnames, files) in os.walk(path + '/' + dirList[i]):
		if files != []:
			print(root, files[i])
		else:
			print(root, files)
		
for i in os.walk(path):
	print(i.name)
	print(i.path)
	print(i.inode())
	print(i.is_dir())
	print(i.is_file())
"""
