import pandas as pd

df = pd.read_csv("input", sep=" ", header=None)
print(df.shape[0])
horizontal = 0
depth = 0
aim = 0
for i in range(df.shape[0]):
	name = df[0][i]
	units = df[1][i]
	if name == "forward":
		horizontal += units
		depth += aim*units
	if name == "down":
		aim += units
	if name == "up":
		aim -= units

print("horizontal:", horizontal, "depth:", depth, "a*b:", horizontal*depth)
