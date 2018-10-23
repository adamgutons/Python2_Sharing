person = {'name': 'Dominic', 'sign': 'positive', 
		'pets':{'dog1':'henry', 'dog2': 'layla'}, 
		'kids':('none','n/a'),
		'age':format((24*7), '.2f')}

# print(person['pets']['dog1'])

while True:
	print('keys: name, pets, kids, age')
	search = input('Enter key to return value, "q" to quit >> ')
	if search == 'q': break
	print(person[search])
