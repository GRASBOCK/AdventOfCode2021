import pandas as pd

df = pd.read_csv("input", sep=" ", header=None)
print(df.shape[0])
horizontal = 0
depth = 0
for i in range(df.shape[0]):
	name = df[0][i]
	units = df[1][i]
	if name == "forward":
		horizontal += units
	if name == "down":
		depth += units
	if name == "up":
		depth -= units

print("horizontal:", horizontal, "depth:", depth, "a*b:", horizontal*depth)
