import numpy

ages = list(numpy.loadtxt("input", delimiter=",", dtype=int))
days = 80
for i in range(days):
	for j in range(len(ages)):
		ages[j] -= 1
		if ages[j] < 0:
			ages[j] = 6
			ages.append(8)
print("number of lanternfish after %i days:"%days, len(ages))