#asks the user to enter a person’s age. Then the program should display text indicating whether the person is an infant, a toddler, a child, a teenager, an adult, or a senior

age = int(input("please state a person's age: "))

'''If less than 1 year old, the person is an infant.
If at least 1 year old but younger than 3, the person is a toddler.
If at least 3 years old but younger than 13, the person is a child.
If at least 13 years old but younger than 18, the person is a teenager.
If at least 18 years old but younger than 65, the person is an adult.
If 65 or older, the person is a senior.'''


if age < 1:
	print("this person's age category: infant")
elif 1 <= age < 3:
	print("this person's age category: toddler")
elif 3 <= age < 13:
	print("this person's age category: child")
elif 13 <= age < 18:
	print("this person's age category: teenager")
elif 18 <= age < 65:
	print("this person's age category: adult")
else:
	print("this person's age category: senior")