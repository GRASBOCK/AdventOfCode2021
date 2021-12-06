import pandas as pd

df = pd.read_csv("input", header=None, dtype="string")
numbers = df[0]
print(numbers)

first_row: str = numbers[0]
num_bits = len(first_row)
high_bits = [0] * num_bits
for number in numbers:
	for bit in range(num_bits):
		#print("bit:", number[bit])
		if number[bit] == '1':
			high_bits[bit] += 1

print("high_bits", high_bits)

most_common = ['0'] * num_bits
for i in range(num_bits):
	if high_bits[i] > len(numbers)/2:
		most_common[i] = '1'
	else:
		most_common[i] = '0'

most_common = "".join(most_common)

gamma_rate_binary = most_common
gamma_rate = int(gamma_rate_binary, base=2)
print("gamma_rate:", gamma_rate, "from", gamma_rate_binary)

# invert gamma rate
epsilon_rate_binary = []
for i in range(num_bits):
	if gamma_rate_binary[i] == '1':
		epsilon_rate_binary.append('0')
	else:
		epsilon_rate_binary.append('1')
epsilon_rate_binary = "".join(epsilon_rate_binary)
epsilon_rate = int(epsilon_rate_binary, base=2)
print("epsilon_rate:", epsilon_rate, "from", epsilon_rate_binary)
result = gamma_rate * epsilon_rate
print(result)
print("1001 = ", int("1001", base=2))