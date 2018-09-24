# w/ help from my classmate Coral, their nice work can be found here: https://github.com/csheldonhess/cit-129/blob/master/week3/JailStats/nocsv.py 
white = 0
black = 0
t = True
writeFile = open('data.txt', 'w')
with open('jail.csv', 'r') as file:
	header = file.readline().rstrip()
	header = header.split(',')
	while t:
		body = file.readline()
		if body == '':
			t = False
		else:
			body = body.rstrip()
			body = body.split(',')
			d = dict(zip(header, body))
			if d['Race'] == 'W':
				white += 1
			if d['Race'] == 'B':
				black += 1
	writeFile.write('Total white = %d\n' % white)
	writeFile.write('Total black = %d' % black)
	print('Count written to data.txt')			

"""
commented code

white = 0
black = 0
# set bool for getting out of read loop
t = True
# make a write file to send data somewhere
writeFile = open('data.txt', 'w')
# open jail.csv file as read file
with open('jail.csv', 'r') as file:
	# take first line in csv by readline(), then strip the \n value
	header = file.readline().rstrip()
	# use split on comma delimtere to make header into own list ['_id', 'Date', 'Gender', etc...]
	header = header.split(',')
	# use print to test header list
	print(header)
	# begin a loop to read through rest of file after first line (readline())
	while t:
		# start reading each line in file after header, store in body var	
		body = file.readline()
		# if we get to end of file by reading, break loop
		if body == '':
			t = False
		else:
			# other wise, take each line and strip \n character
			body = body.rstrip()
			# then take body which is stripped of \n and split to make a list of each line
			body = body.split(',')
			# use zip to make header the keys and body (data) will become the values
			d = dict(zip(header, body))
			# can make our counts.  we can find other data as well by passing in different keys
			if d['Race'] == 'W':
				white += 1
			if d['Race'] == 'B':
				black += 1
	writeFile.write('Total white = ' + str(white) + '\n')
	writeFile.write('Total black = ' + str(black) + '\n')
	print('Count written to data.txt')			

"""