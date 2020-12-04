import math
inp = []
#inp = ['1969']

if inp == []:
	with open("1.txt", "r") as f:
		inp = f.read().splitlines()


def solution_1():
	sol = []
	for mass in inp:
		mass = int(mass) / 3
		mass = math.floor(mass)
		mass = mass - 2
		sol.append(mass)


	return sum(sol)

def solution_2():
	sol = []
	for mass in inp:
		fuel = int(mass) // 3 -2

		_fuel = the_deed(fuel)
		#print("mass fuel:", fuel)
		#print("Fuel fuel:", _fuel)
		sol.append(fuel);sol.append(_fuel)
	return sum(sol)

def the_deed(mass):
	fuel = 0
	while mass // 3 -2 > 0:
		mass = mass // 3 - 2
		fuel += mass
	return fuel
		

print("SOLUTION1:", solution_1())
print("SOLUTION2:", solution_2())