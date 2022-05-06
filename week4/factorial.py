#prints factorial of the value the user inputs
#note: if user inputs 0, the for loop should not run, so product = 1
num = int(input("enter a number: "))

product = 1
for x in range(num, 1, -1):
	product *= x

print(num, "! = ", product, sep='')