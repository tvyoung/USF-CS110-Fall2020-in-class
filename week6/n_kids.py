#reads the data from n_kids.txt, does some math, then displays the following:
'''Total number of families:
Total number of kids:
Average number of kids per family:
Maximum number of kids in a family:
Minimum number of kids in a family:'''

readFile = open("n_kids.txt", "r")

#total lines = total number of families input in n_kids.txt file
totalLines = 0
totalKids = 0
maximumKids = 0
minimumKids = 1

for line in readFile:
	kids = int(line)
	totalKids += kids

	if kids > maximumKids:
		maximumKids = kids
	elif kids < minimumKids:
		minimumKids = kids

	totalLines += 1

readFile.close()

average = totalKids/totalLines

print("total number of families:", totalLines)
print("total number of kids:", totalKids)
print("average number of kids per family:", format(average, '.2f'))
print("maximum number of kids in a family:", maximumKids)
print("minimum number of kids in a family:", minimumKids)


'''Extra credit (2 pts): write the above results to a different file (results.txt, not to the input file n_kids.txt) in addition to displaying them on the screen. Do not use built in min and max functions.'''

writeFile = open("results.txt", "w")
writeFile.write("total number of families: " + str(totalLines) + "\n")
writeFile.write("total number of kids: " + str(totalKids) + "\n")
writeFile.write("average number of kids per family: " + str(format(average, '.2f')) + "\n")
writeFile.write("maximum number of kids in a family: " + str(maximumKids) + "\n")
writeFile.write("minimum number of kids in a family: " + str(minimumKids) + "\n")