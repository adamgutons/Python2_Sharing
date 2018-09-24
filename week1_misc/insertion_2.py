l = [4,1,3,6,7,5,2]
for x in range(1,len(l)):
	key = l[x]
	i = x
	while i > 0 and l[i-1] > key:
		l[i] = l[i-1]
		i = i - 1
	l[i] = key
	print(key)
print(l)	                                                                                                  