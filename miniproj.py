# made by Adam Gutonski. free to all living organisms 
#!/usr/bin/env python
def main():
	a = {1:[1], 
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
			delete_from_dict(a)
		else:
			print('invalid entry')	

def display_dict(dic):
	for x in sorted(dic):
		print(x, dic[x])
	print()

def add_to_dict(dic):
	for x in sorted(dic):
		print(x, dic[x])
	try:	
		choice = int(input('Where to add items 1-3? 4 to return >> '))
		if choice == 4: return
		if type(dic[choice]) == type([]):
			new_element = input('What to add? >> ')
			if new_element.isdigit():
				new_element = int(new_element)
			dic[choice].append(new_element)
			print('dictionary updated...\n')
			return
		if type(dic[choice]) == type({}):
			print(dic[choice])
			print('Add to which key?')
			key = (input('>> '))
			new_value = input('What to add? >> ')
			if new_value.isdigit():
				new_value = int(new_value)
			dic[choice][key].append(new_value)
			print('dictionary updated...\n')
			return	
		print('dictionary updated...\n')
	except:
		print('invalid...\n')

def delete_from_dict(dic):
	for x in sorted(dic):
		print(x, dic[x])
	try:	
		choice = int(input('Delete from which items 1-3? 4 to return >> '))
		if choice == 4: return
		if type(dic[choice]) == type([]):
			remove_element = int(input('Which item to delete? (enter a number) >> '))
			remove_element = remove_element - 1
			if remove_element == dic[choice].index(dic[choice][-1]):
				print("Removing the last item is forbidden...")
				print()
				return
			dic[choice].pop(remove_element)
			print('dictionary updated...')
			return
		if type(dic[choice]) == type({}):
			print(dic[choice])
			print('Delete from which key?')
			key = (input('>> '))
			remove_element = int(input('Which item to delete? (enter a number) >> '))
			remove_element = remove_element - 1
			if remove_element == dic[choice][key].index(dic[choice][key][-1]):
				print("Removing the last item is forbidden...")
				return print()
			dic[choice][key].pop(remove_element)
			print('dictionary updated...')
			return
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
