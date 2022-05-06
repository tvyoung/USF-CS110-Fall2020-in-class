#asks for temperature of water in fahrenheit, states whether that is a solid/liquid/gas. returns answer in celsius.

fahrenheitTemperature = float(input("what is the temperature of the water in Fahrenheit? "))

'''Facts: At sea level, water freezes at 32 degrees F and boils at 212 degrees F.

gas: water >= 212 F
liquid: 32 < water < 212 F
solid: water <= 32 F

gas: water >= 100 C
liquid: 0 < water < 100 C
solid: water <= 0 C

32 F = 0 C and 212 F = 100 C'''

celsiusTemperature = (5/9) * (fahrenheitTemperature - 32)

if celsiusTemperature >= 100.00:
	print("water at the temperature ", format(celsiusTemperature, '.2f'), "°C is a gas.", sep='')
elif celsiusTemperature > 0.00:
	print("water at the temperature ", format(celsiusTemperature, '.2f'), "°C is a liquid.", sep='')
else:
	print("water at the temperature ", format(celsiusTemperature, '.2f'), "°C is a solid.", sep='')