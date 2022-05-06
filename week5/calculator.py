#asks user for two numbers and a mathematical operation (+, -, *, /)
#displays the result of performing operation on the two given numbers

def main():
	#creates local variable repeat and assigns it 'y' so that the while loop can run
	repeat = "y"
	#introduction
	print("welcome to the Calculator Program!")
	#loops calculator program as long as user continues to enter 'y' or 'Y'
	while repeat == "y" or repeat == "Y":
		#asks user for two numbers and stores in two different variables
		num1 = float(input("please input your first number: "))
		num2 = float(input("please input your second number: "))
		#asks user for mathematical operation
		operation = input("please enter a mathetmatical operation (+, -, *, /): ")

		#calls specific function of respective operation symbol
		#displays an error message if the user enters an invalid operation symbol. will not ask user to enter an appropriate input again.
		if operation == "+":
			add(num1, num2)
		elif operation == "-":
			subtract(num1, num2)
		elif operation == "*":
			multiply(num1, num2)
		elif operation == "/":
			divide(num1, num2)
		else: 
			print("ERROR: invalid operation system.")

		#asks the user if they want to continue
		#will ask for two new numbers and a mathematical operation if user enters 'y' or 'Y' 
		repeat = input("to perform another operation, enter 'y' or 'Y': ")

#performs addition
def add(x, y):
	result = x + y
	print(x, "+", y, "=", result)

#peforms subtraction
def subtract(x, y):
	result = x - y
	print(x, "-", y, "=", result)

#performs multiplication
def multiply(x, y):
	result = x * y
	print(x, "*", y, "=", result)

#performs division
def divide(x, y):
	result = x /y
	print(x, "/", y, "=", result)

main()