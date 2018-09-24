a = [5,3,4,2,1]
for x in range(len(a)-1,0,-1):
	for j in range(x):
		if a[j] > a [j+1]:
			temp = a[j]
			a[j] = a[j+1]
			a[j+1] = temp
print(a)
