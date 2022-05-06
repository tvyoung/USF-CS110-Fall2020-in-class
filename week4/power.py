#prompts the user for two numbers: a base and an exponent, and computes the power using the base and exponent using a while loop (and not the ** operator!)

base = int(input("enter a base: "))
exponent = int(input("enter an exponent: "))

#ex. base = 2, exponent = 10, power = 1024

i = 0
power = 1
while i < exponent:
	power *= base
	i += 1
print(base, "to the power", exponent, "is", power)