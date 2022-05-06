#iterates through the list of lists hr and calculate the average of each sub-list
#appends the average of each sub-list to a new list as iterates through hr.
#prints this list of average heart rates at the end

hr = [ [ 72, 75, 71, 73],      # resting
[ 91, 90, 94, 93],             # walking slowly
[ 130, 135, 139, 142],         # running on treadmill
[ 120, 118, 110, 105, 100, 98] # after a minute recovery
]

#alternative:
'''averageResting = 0
averageWalking = 0
averageRunning = 0
averageRecovery = 0'''

averages = [0] * 4

for rows in range(len(hr)):
	for columns in range(len(hr[rows])):
		averages[rows] = averages[rows] + hr[rows][columns]
	averages[rows] = averages[rows] / len(hr[rows])


print(averages)

