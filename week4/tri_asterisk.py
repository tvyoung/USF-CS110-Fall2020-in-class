#uses nested for loops to draw this pattern (that’s 10 *s in the top row and 10 columns long)

for rows in range(10):
	for columns in range(11-(rows+1)):
		print("*", end='')
	print("")



#rows ten
	#each row should have 10-n
	#n = row number