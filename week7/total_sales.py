#asks the user to enter a store’s sales for each day of the week and then calculates the total sales for the week and displays the result

daily_sales = [0.0] * 7
days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

i = 0
while i < len(days_of_week):
	print("enter the sales for ", days_of_week[i], ": ", sep='', end='')
	daily_sales[i] = float(input())
	i += 1


total = 0
i = 0
while i < len(daily_sales):
	total += daily_sales[i]
	i += 1

print("total sales for the week: $" + format(total, '.2f'))
