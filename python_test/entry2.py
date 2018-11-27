def write_commissions():
	write_file = open('commissions.txt', 'w')
	stop_calc = True

	while(stop_calc):

		sales_name = input("What is your name? >> ")
		salary = float(input("What is your salary? >> "))

		newString = '%s$%.2f\n' % (sales_name, salary)
		write_file.write(newString)
		print('data written to file...')

		stop_loop = input("Enter another salary record? (y for yes, n for no) >> ")
		
		if stop_loop == 'n':
			stop_calc = False
			print("Program exiting...\n")
			write_file.close()


def read_commissions():
	salary_list = []
	read_file = open('commissions.txt', 'r')
	for line in read_file:
		salary_list.append(line.rstrip())
	read_file.close()

	return salary_list

def calc_commissions(salary_list):
	SALARY_BOUND_1 = 50000
	SALARY_BOUND_2 = 100000
	COMM_RATE_1 = .02
	COMM_RATE_2 = .03
	COMM_RATE_3 = .05

	print("--- COMMISSIONS REPORT ---\n")
	for x in salary_list:
		j = x.split('$')
		name = j[0]
		salary = float(j[1])
		if salary <= SALARY_BOUND_1:
			print("%s\nSalary $%.2f Commissions $%.2f" % (name, salary, salary * COMM_RATE_1))
		elif salary > SALARY_BOUND_1 and salary <= SALARY_BOUND_2: 
			print("%s\nSalary $%.2f Commissions $%.2f" % (name, salary, salary * COMM_RATE_2))
		elif salary > SALARY_BOUND_2:
			print("%s\nSalary $%.2f Commissions $%.2f" % (name, salary, salary * COMM_RATE_3))

def main():
	
	write_commissions()
	salary_list = read_commissions()
	calc_commissions(salary_list)

main()
