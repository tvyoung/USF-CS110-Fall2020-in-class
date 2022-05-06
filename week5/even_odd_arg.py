#takes in an argument n that prints “This is an even number” or “This is an odd number”

#gets an integer number from the user and call even_or_odd(n) and pass in the user’s input
def main():
	number = int(input("please state a number: "))
	even_or_odd(number)

#takes argument n and determines whether n is even or odd
def even_or_odd(n):
	if n % 2 == 0:
		print("this is an even number.")
	else:
		print("this is an odd number.")

main()