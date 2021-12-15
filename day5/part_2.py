import numpy

file = open('input', 'r')
line_strings = file.readlines()

# Strips the newline character
lines = []
width = 1
height = 1
for line_str in line_strings:
	points = line_str.replace('\n', '').split(" -> ")
	[[x1, y1], [x2, y2]] = [point.split(",") for point in points]
	line = [ int(v) for v in [x1, y1, x2, y2]]
	lines.append(line)
	[x1, y1, x2, y2] = line
	if x1 >= width:
		width = x1 + 1
	if y1 >= height:
		height = y1 + 1
	if x2 >= width:
		width = x2 + 1
	if y2 >= height:
		height = y2 + 1
	#print("line: ", line)

print("width: ", width, " height: ", height)

points = numpy.array([[0 for i in range(width)] for i in range(height)])
for line in lines:
	[x1, y1, x2, y2] = line
	if y1 == y2: # horizontal 
		for x in range(min([x1, x2]), max([x1, x2]) + 1):
			points[y1][x] += 1
	elif x1 == x2: # vertical
		for y in range(min([y1, y2]), max([y1, y2]) + 1):
			points[y][x1] += 1
	else: # diagonal
		x_len = x2 - x1
		y_len = y2 - y1
		dx = numpy.sign(x_len)
		dy = numpy.sign(y_len)
		x = x1
		y = y1
		for i in range(numpy.abs(x_len) + 1):
			points[y][x] += 1
			x += dx
			y += dy

#print("points:\n", points)

print("overlap occurences:", numpy.count_nonzero(points > 1))