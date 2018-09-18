print('Challenge 1:')
for x in range(0,101,2):
	print(x, end=' ')
print()
print()
print('Challenge 2:')
k = ''.join([x * 3 for x in 'KABOOM'])
for x in k:
	print(x, end=' ')
print()
print()
print('Challenge 3:')
for x in "askaliceithinkshe'llknow"[::2]:
	print(x, end=' ')
print()
print()
print('Challenge 4:')
for x in range(1,5):
	for i in range(5,8):
		print(x, '|', i, '|', x*i)
print()
print()
print('Challenge 5:')
l = [['mn', 'pa', 'ut'], ['b','p','c'], ['echo','tango','charlie']]
labels = {'state':'US State Abbr:', 'element':'Chemical Element:', 'alpha':'Phonetic Call:'}
for i in range(len(l)):
	for x in range(len(l)):
		if len(str(l[i][x])) < 2:
			print(labels['element'], l[i][x].upper())
		elif len(str(l[i][x])) == 2:
			print(labels['state'], l[i][x].upper())
		else:
			print(labels['alpha'], l[i][x].upper())