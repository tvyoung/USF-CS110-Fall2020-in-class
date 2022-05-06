#write three different versions of your own factorial function
#Do not use the math.factorial() function in your own factorial functions
#factorial functions should return their computed value; they should not print their value
#include a main() function that calls your factorial functions with test-numbers

def main():
	#testing factorial_while(n) with n = 5
	print("solve 5! using while loop:", factorial_while(5))
	#test with n = 4
	print("solve 4! using while loop:", factorial_while(4))
	#test with n  = 0
	print("solve 0! using while loop:", factorial_while(0))


	#testing factorial_for(n) with n = 6
	print("solve 6! using for loop:", factorial_for(6))
	#test with n = 3
	print("solve 3! using for loop:", factorial_for(3))
	#test with n = 0
	print("solve 0! using for loop:", factorial_for(0))

	#testing factorial_recurse(n) with n = 7
	print("solve 7! using recursion:", factorial_recurse(7))
	#testing with n = 2
	print("solve 2! using recursion:", factorial_recurse(2))
	#testing with n = 0
	print("solve 0! using recursion:", factorial_recurse(0))


#using a while loop
def factorial_while(n):
	product = 1
	while n > 0:
		product *= n
		n -= 1
	return product

#using a for loop
def factorial_for(n):
	product = 1
	for i in range (n, 0, -1):
		product *= i
	return product
	
#using recursion
def factorial_recurse(n):
	if n == 0:
		return 1
	else:
		return n * factorial_recurse(n-1)


main()