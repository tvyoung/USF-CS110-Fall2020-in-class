#Gets in the original price of an item as input.
originalPrice = float(input("what is the original price of the item? (please input in the format 00.00) "))

#Calculates the discounted price with a 40% discount.
discount = originalPrice * 0.4
salePrice = originalPrice - discount

#Prints the sale prices as output in the correct format (ex: $2.45).
print("the sale price of the item is $", format(salePrice, ',.2f'), sep='')