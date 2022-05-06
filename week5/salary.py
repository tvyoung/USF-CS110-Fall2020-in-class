#offers two options to receive salary, constant salary and doubling salary

#calls both functions and states the values for each salary.
#compare the totals that are returned and determine which salary option is better.
def main():
	print("comparing the two given options to receive salary for ten days.")
	option1 = constant_salary()
	option2 = doubling_salary()
	print("the total income from the constant salary is: $", option1, sep='')
	print("the total income from the doubling salary is: $", option2, sep='')
	difference = option2 - option1
	print("the income from the doubling salary is greater by $", difference, sep='')
	print("in conclusion, the doubling salary is the better option.")

#Constant Salary: Receive $100 each day for 10 days
#computes the total income for option 1 and returns the total
def constant_salary():
	print("option 1, constant salary: receive $100 each day for 10 days.")
	return 100 * 10

#Doubling Salary: $1 the first day, $2 the second day, $4 the third day, $8 the fourth day, doubling the amount each day, for 10 days.
#computes the total income for option 2 and returns the total
def doubling_salary():
	print("option 2, doubling salary: $1 the first day, $2 the second day, $4 the third day, $8 the fourth day, doubling the amount each day, for 10 days.")
	total = 0
	for day in range(1, 11):
		total += 2**(day-1)
		#for testing
		#print(day, "---", total)
	return total

main()
