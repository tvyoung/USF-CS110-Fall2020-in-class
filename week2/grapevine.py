#program calculates and displays number of grapevines that will fit in a row


#INPUT 
#length of the row, in feet
length = float(input("enter the length of the row, in feet: "))
#amount of space used by an end-post assembly, in feet
e = float(input("enter the amount of space, in feet, used by an end-post assembly: "))
#amount of space between the vines, in feet
distanceBetween = float(input("enter the distance, in feet, between each vine: "))


#CALCULATIONS
#formula is V=(R-2E)/S 
totalGrapevines = (length - 2 * e) / distanceBetween


#DISPLAY
print("you have enough space for", format(totalGrapevines, '.2f'), "vines.")