currency = input("Currency to convert to U.S. dollars: e = Euros, c= Chinese Yuan, r = Indian Rupees, b = Bitcoin: ")

if currency == "e":
	amount = float(input("amount of Euros to convert: "))
	conversion = amount * 1.16
	print("in U.S. dollars, that is $", format(conversion, ',.2f'), sep='')
elif currency == "c": 
	amount = float(input("amount of Chinese Yuan to convert: "))
	conversion = amount * 0.15
	print("in U.S. dollars, that is $", format(conversion, ',.2f'), sep='')
elif currency == "r":
	amount = float(input("amount of Indian Rupees to convert: "))
	conversion = amount * 0.015
	print("in U.S. dollars, that is $", format(conversion, ',.2f'), sep='')
elif currency == "b":
	amount = float(input("amount of Bitcoin to convert: "))
	conversion = amount * 6923.80
	print("in U.S. dollars, that is $", format(conversion, ',.2f'), sep='')
else: 
	print("sorry, that isn't a valid input.")