def calc_commission():
	SALARY_BOUND_1 = 50000
	SALARY_BOUND_2 = 100000
	COMM_RATE_1 = .02
	COMM_RATE_2 = .03
	COMM_RATE_3 = .05
	stop_calc = True

	while(stop_calc):

		sales_name = input("What is your name? >> ")
		salary = float(input("What is your salary? >> "))

		if salary <= SALARY_BOUND_1:
			print("%s\nSalary: $%.2f Commission: $%.2f" % (sales_name, salary, (salary * COMM_RATE_1)))
		elif salary > SALARY_BOUND_1 and salary <= SALARY_BOUND_2:
			print("%s\nSalary: $%.2f Commission: $%.2f" % (sales_name, salary, (salary * COMM_RATE_2)))
		elif salary > SALARY_BOUND_2:
			print("%s\nSalary: $%.2f Commission: $%.2f" % (sales_name, salary, (salary * COMM_RATE_3)))
		else:
			print('sorry, please try again.')

		stop_loop = input("Enter another salary record? (y for yes, n for no) >> ")
		
		if stop_loop == 'n':
			stop_calc = False
			print("Program exiting...")

			
def main():

	calc_commission()

main()
