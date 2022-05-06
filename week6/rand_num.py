#writes a series of random numbers to a file rand_num.txt one number per line. 
#Each random number should be in the range of 1 through 500.
#The application should ask the user how many random numbers the file will hold with ‘How many random numbers would you like?’
import random

writeFile = open("rand_num.txt", "w")

totalNumbers = int(input("how many random numbers would you like? "))

for i in range(totalNumbers):
	line = random.randint(1, 500)
	writeFile.write(str(line) + "\n")

writeFile.close()