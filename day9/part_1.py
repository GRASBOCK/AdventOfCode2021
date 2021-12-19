import numpy

file = open('input_test', 'r')
file_contents = file.read()
heightmap = [[]]

row = 0
for char in file_contents:
	if char.isnumeric():
		heightmap[row].append(int(char))
	elif char == "\n":
		row += 1
		heightmap.append([])

heightmap.remove([]) # remove empty lists
heightmap: numpy.ndarray = numpy.array(heightmap)
print(heightmap)
(ymax, xmax) = heightmap.shape

def check_minimal(valid, height, y, x):
	global minimal, heightmap
	if valid:
		other_height = heightmap[y][x]
		if other_height <= height:
			minimal = False

total_risk_level = 0
for y in range(ymax):
	for x in range(xmax):
		height = heightmap[y][x]

		(top, left, bottom, right) = (True, True, True, True)
		if x == 0:
			left = False
		if x == xmax - 1:
			right = False
		if y == 0:
			top = False
		if y == ymax - 1:
			bottom = False

		#print(top, left, bottom, right)
		#print((x, y))
		minimal = True
		check_minimal(top, height, y - 1, x)
		check_minimal(bottom, height, y + 1, x)
		check_minimal(left, height, y, x - 1)
		check_minimal(right, height, y, x + 1)

		if minimal:
			total_risk_level += height + 1
print("the total risk level is", total_risk_level)