a = [12,4,6,1,8,3,2,5,6,7,10,11,3]
for x in range(1,len(a)):	# start at 1 to get 2nd index position, iteration through list length
	key = a[x]				# mathc 
	i = x 
	while i > 0 and a[i-1] > key:
		a[i] = a[i-1]		# swap occurs here if i > 0 and the index position of 1 is > key (2 at first loop)
		i = i - 1
	a[i] = key
print()
print(a)
