import numpy
from numba import jit

# the challenge of part 2 is to make it fast (it takes forever otherwise)
# still takes to long even with numba (maybe I don't really know how to use it yet)
ages: numpy.ndarray = numpy.loadtxt("input_test", delimiter=",", dtype=int)

new_fish = 0

@jit(nopython=True, parallel = True)
def simulate(ages: numpy.ndarray):
	new_fish = 0
	for j in range(len(ages)):
		ages[j] -= 1
		if ages[j] < 0:
			ages[j] = 6
			new_fish += 1
	new_fish_ages = numpy.full((new_fish), 8)
	return numpy.append(ages, new_fish_ages)

days = 256
for i in range(days):
	ages = simulate(ages)
	print("day %i: %i fish"%(i+1, len(ages)))
print("number of lanternfish after %i days:"%days, len(ages))