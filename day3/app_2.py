import pandas as pd

df = pd.read_csv("input", header=None, dtype="string")
numbers = df[0]
print(numbers)

first_row: str = numbers[0]
num_bits = len(first_row)

def count_high_bits(numbers: 'list[str]', bit_pos: int):
	high_bits = 0
	for number in numbers:
		if number[bit_pos] == '1':
			high_bits += 1
	return high_bits

def filter_at_bit_pos(numbers: 'list[str]', bit_pos: int, value: str):
	filtered_list = []
	for number in numbers:
		if number[bit_pos] == value:
			filtered_list.append(number)
	return filtered_list

def most_common_at_bit_pos(numbers: 'list[str]', bit_pos: int):
	print(count_high_bits(numbers, bit_pos), len(numbers)/2)
	if count_high_bits(numbers, bit_pos) >= len(numbers)/2:
		return '1'
	return '0'

# oxygen generator rating
oxygen_generator_list = numbers.copy()
for bit in range(num_bits):
	if len(oxygen_generator_list) == 1:
		break
	else:
		most_common = most_common_at_bit_pos(oxygen_generator_list, bit)
		oxygen_generator_list = filter_at_bit_pos(oxygen_generator_list, bit, most_common)
		print(oxygen_generator_list)
assert(len(oxygen_generator_list) == 1, "Not unique oxygen generator rating")
oxygen_generator_rating = int(oxygen_generator_list[0], base=2)
print("oxygen_generator_rating", oxygen_generator_rating)

# co2 scrubber rating
co2_scrubber_list = numbers.copy()
for bit in range(num_bits):
	if len(co2_scrubber_list) == 1:
		break
	else:
		most_common = most_common_at_bit_pos(co2_scrubber_list, bit)
		if most_common == '1':
			filter_value = '0'
		else:
			filter_value = '1'
		co2_scrubber_list = filter_at_bit_pos(co2_scrubber_list, bit, filter_value)

assert(len(co2_scrubber_list) == 1, "Not unique co2 scrubber rating")
co2_scrubber_rating = int(co2_scrubber_list[0], base=2)
print("co2_scrubber_rating", co2_scrubber_rating)

result = co2_scrubber_rating * oxygen_generator_rating
print("result:",result)