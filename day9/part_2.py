import numpy

file = open('input', 'r')
file_contents = file.read()
heatmap = [[]]

row = 0

basin = -2
wall = -1

for char in file_contents:
	if char == "9":
		heatmap[row].append(wall)
	elif char.isnumeric():
		heatmap[row].append(basin)
	elif char == "\n":
		row += 1
		heatmap.append([])

heatmap.remove([]) # remove empty lists
heightmap: numpy.ndarray = numpy.array(heatmap)
(ymax, xmax) = heightmap.shape

def is_basin(valid, y, x):
	global heightmap, basin
	if valid:
		value = heightmap[y][x]
		if value == basin:
			return True
	return False

basins = []
def flood_fill(y, x, index):
	global basins, heightmap, xmax, ymax

	basins[index] += 1
	heightmap[y, x] = index

	(top, left, bottom, right) = (True, True, True, True)
	if x == 0:
		left = False
	if x == xmax - 1:
		right = False
	if y == 0:
		top = False
	if y == ymax - 1:
		bottom = False
	
	next = lambda valid, y, x, index: flood_fill(y, x, index) if is_basin(valid, y, x) else None
	next(top, y - 1, x, index)
	next(bottom, y + 1, x, index)
	next(left, y, x - 1, index)
	next(right, y, x + 1, index)

for y in range(ymax):
	for x in range(xmax):
		value = heightmap[y][x]
		if value == basin:
			index = len(basins)
			basins.append(0)
			flood_fill(y, x, index)

largest_three_basins = sorted(basins, reverse=True)[0:3]
result = 1
for basin_size in largest_three_basins:
	result *= basin_size
print("basin sizes of the three largest multiplied together =", result)