bound = int(input("Enter upper list bound >> "))
z = 0
l = []
for x in range(bound):
	l.append(x)
print(l)
for x in l:
	z += x
print(z)