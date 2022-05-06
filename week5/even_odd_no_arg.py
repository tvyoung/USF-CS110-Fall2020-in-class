#asks for user input, and based on the user’s input, prints ‘This is an even number’ or ‘This is an odd number’.

def main():
	even_or_odd()

#asks for user to input a number
#determines whether it is even or odd
def even_or_odd():
	number = int(input("please state a number: "))
	if number % 2 == 0:
		print("this is an even number.")
	else:
		print("this is an odd number.")

main()