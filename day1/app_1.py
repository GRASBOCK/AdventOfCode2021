import numpy
test_depths = numpy.array([
199,
200,
208,
210,
200,
207,
240,
269,
260,
263,])

depths = numpy.loadtxt("input.txt")

print(depths)
increased = 0
for i in range(1, len(depths)):
	if depths[i] > depths[i-1]:
		increased += 1
print(increased)