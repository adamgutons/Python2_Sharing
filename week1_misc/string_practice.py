entry = input("Enter a string >> ")
if len(entry) < 4:
	print('BAD!!')
	exit()
if entry[0] == entry[-1]:
	print('first and last are the same! spooky!')
x = input('Enter first string >> ')
y = input('Enter second string >> ')
z = input('Enter third string >> ')
l = []
l.extend([x,y,z])
l.sort()
for x in l:
	print(x, end=' ')