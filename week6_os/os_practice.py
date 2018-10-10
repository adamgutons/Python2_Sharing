import os

path = os.environ['HOME'] + '/weebly'
#path = "/home/techred3/weebly"

for (root, dirnames, files) in os.walk(path):
	fileList = files
	dirList = dirnames
	print('DIRECTORIES', dirList, 'FILES', fileList)
"""		
for i in os.walk(path):
	print(i.name)
	print(i.path)
	print(i.inode())
	print(i.is_dir())
	print(i.is_file())
"""
