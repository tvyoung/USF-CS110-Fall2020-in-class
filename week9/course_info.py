#allows the user to enter the name of a course and receive details of its room number, instructor, and time

def main():
	#course numbers and the room numbers of the rooms where the course meets
	courseRooms = { "CS110" : "3004", 
					"CS112" : "4501",
					"CS220" : "6755",
					"CS245"	: "1244",
					"CS212"	: "1411" }

	#course numbers and the names of the instructors that teach each course
	courseInstructors = { "CS110" : "Haynes",
						  "CS112" : "Alvarado",
						  "CS220" : "Rich",
						  "CS245" : "Burke",
						  "CS212" : "Lee" }

	#instructors and the meeting times of each course
	instructorTimes = { "Haynes"   : "8AM",
						"Alvarado" : "9AM",
						"Rich"     : "10AM",
						"Burke"    : "11AM",
						"Lee"      : "12PM" }

	#asks user to input a course number
	course = input("enter a course number: ")

	#if course is not valid, prints error message
	if course not in courseRooms:
		print(course, "is an invalid course number.")

	#get the instructor name of the course
	instructor = courseInstructors[course]

	#display the course’s room number, instructor, and meeting time
	print("the details for the course", course, "are:")
	print("room:", courseRooms[course])
	print("instructor:", instructor)
	print("time:", instructorTimes[instructor])


main()