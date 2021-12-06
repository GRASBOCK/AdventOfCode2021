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

def sliding_window_sum(i):
	sum_window = 0
	for j in range(0, sliding_window_size):
		sum_window += depths[i - j]
	return sum_window

increased = 0
sliding_window_size = 3
for i in range(sliding_window_size, len(depths)):
	sum_a = sliding_window_sum(i)
	sum_b = sliding_window_sum(i-1)

	if sum_a > sum_b:
		increased += 1
print(increased)