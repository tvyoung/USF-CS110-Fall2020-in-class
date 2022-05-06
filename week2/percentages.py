'''program asks the user for the number of males and the number of females registered in a class.
displays the percentage of males and females in the class to 2 decimal places along with the % sign.'''

males = int(input("number of males registered in the class: "))
females = int(input("number of females registered in the class: "))

#total number of students in the class
total = males + females

#calculations
percentageMale = float((males/total) * 100)
percentageFemale = float((females/total) * 100)

#percentages displayed to 2 decimal places
print("the percentage of males in the class: ", format(percentageMale, '.2f'), "%", sep='')
print("the percentage of females in the class: ", format(percentageFemale, '.2f'), "%", sep='')