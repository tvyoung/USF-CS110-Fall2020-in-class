#program converts a given temperature in Celsius to Fahrenheit

#Input the temperature in Celsius
celsiusTemperature = float(input("please input the temperature in Celsius (format 00.00) "))

#conversion calculations
fahrenheitTemperature = (9/5) * celsiusTemperature + 32

#output fahrenheit to 2 decimal places
print("temperature in fahrenheit is:", format(fahrenheitTemperature, '.2f'), "°F")
