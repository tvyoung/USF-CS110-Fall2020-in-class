'''user enters two names. print them in sorted order, lowest to highest (lowest means the word with the lowest ASCII code value, e.g., Mark < Mary ), i.e. in alphabetical order. print it in the format: firstname, secondname.'''

name1 = input("please input a name. ")
name2 = input("please input a second name. ")

order = name1 < name2

if order: 
	print(name1, name2)
else:
	print(name2, name1)	