# made by Adam Gutonski. free to all living organisms 
#!/usr/bin/env python
def main():
	a = {1:'adam', 
		 2:['michael', 'henry'], 
		 3:{'dogs':['jake','maggie'], 'cats':['fritz','pam']}}
	while True:
		print('1. Dictionary Info\n2. Add to  Dictionary\n3. Delete from Dictionary\n4. Quit')
		choice = int(input('>> '))
		if choice == 4: 
			print('Qutting...')
			break
		elif choice == 1:
			display_dict(a)
		elif choice == 2: 
			add_to_dict(a)
		elif choice == 3:
			print('delete from to come')
		else:
			print('invalid entry')	

def display_dict(dic):
	for x in sorted(dic):
		print(x, dic[x])
	print()

def add_to_dict(dic):
	for x in sorted(dic):
		print(x, dic[x])
	choice = int(input('Where to add items? >> '))
	try:
		if type(dic[choice]) == type([]):
			new_element = input('What to add? >> ')
			dic[choice].append(new_element)
			print('dictionary updated...')
			return
		if type(dic[choice]) == type({}):
			print(dic[choice])
			print('Add to which key?')
			key = (input('>> '))
			new_value = input('What to add? >> ')
			dic[choice][key].append(new_value)
			print('dictionary updated...')
			return	
		new_items = input('What to add? >> ')
		if new_items.isdigit() & len(new_items) == 1:
			new_items = int(new_items)
		dic[choice] = new_items
		print('dictionary updated...')
	except:
		print('invalid...')
main()







"""
while True:	 
	if x not in a.keys():
		print('not found')
		x = int(input('Which dictionary to access? 1, 2, or 3 >> '))
	else:
		print(a[x])
		x = int(input('Which dictionary to access? 1, 2, or 3 >> '))
"""
