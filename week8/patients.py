#iterates through the list of lists, patients
#appends the last name of all female patients to a new list female_patients and displays female_patients.

patients = [ ['Milos', 'Jones', 48, 'male', 'smoker', 210], 
             ['Delia', 'Chan', 39, 'female', 'non-smoker', 170], 
             ['Dan', 'Ross', 62, 'male', 'non-smoker', 200],
             ['Samantha', 'Tan', 28, 'female', 'non-smoker', 180] ]

#has only the last names of female patients
female_patients = []

for person in range(len(patients)):
	if patients[person][3] == "female":
		female_patients.append(patients[person][1])

print(female_patients)