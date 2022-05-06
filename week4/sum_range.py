#prompts the user for two integers: a and b, and computes the sum of all integers greater than or equal to a and less than or equal to b
#if a is not less than b, program should print out an error message

lower = int(input("Enter an integer for the lower limit: "))
upper = int(input("Enter an integer for the upper limit: "))

sum = 0
if lower < upper:
	for x in range(lower,upper+1):
		sum += x
	print("the sum from", lower, "to", upper, "is", sum)
elif lower == upper:
	print("error:", lower, "=", upper)
else:	
	print("error:", lower, ">", upper)
