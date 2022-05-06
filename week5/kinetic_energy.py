#asks the user to enter values for mass and velocity, then calls the kinetic_energy function to get the object’s kinetic energy
#print to 2 decimal places
def main():
	mass = float(input("enter the moving object's mass in kilograms: "))
	velocity = float(input("enter the moving object's velocity in meters per second: "))
	answer = kinetic_energy(mass, velocity)
	print("the moving objects kinetic energy is:", format(answer, '.2f'), "Joules")

#accepts an object’s mass (in kilograms) and velocity (in meters per second) as arguments
#function should return the amount of kinetic energy that the object has
def kinetic_energy(mass, velocity):
	return (mass * (velocity**2)) / 2

main()