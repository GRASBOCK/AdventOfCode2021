import numpy

horizontal_positions: numpy.ndarray = numpy.loadtxt("input", delimiter=",", dtype=numpy.int32)
min_pos = horizontal_positions.min()
max_pos = horizontal_positions.max()

min_fuel_cost = numpy.iinfo(numpy.int32).max
for pos in range(min_pos, max_pos + 1):
	fuel_cost = 0
	for hpos in horizontal_positions:
		moves = abs(pos - hpos)
		fuel = int(numpy.rint((moves*moves + moves)/2))
		fuel_cost += fuel
		#print("Move from %i to %i: %i fuel"%(hpos, pos, fuel))
	if fuel_cost < min_fuel_cost:
		min_fuel_cost_position = pos
		min_fuel_cost = fuel_cost

print("cheapest position:",min_fuel_cost_position, "fuel cost:",min_fuel_cost)