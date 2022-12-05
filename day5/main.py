def part_one(file):
	input = open(file, 'r')
	Lines = input.readlines()
 
	crate_lines = []
	 
	for line in Lines:
		if line.strip():
			crate_lines.append(line)
		else:
			break
	number_of_stacks = len(crate_lines[-1].strip().split())
	crate_lines = crate_lines[:-1]
	layer = 0
	crates = [['' for x in range(number_of_stacks-1)] for y in range(len(crate_lines)+1)]
	for i in range(len(crate_lines)-1, -1, -1):
		for j in range(1, number_of_stacks+1):
			try:
				crate_contents = crate_lines[i][4*j-3]
				crates[j-1][layer] = crate_contents
			except IndexError:
				pass
		layer +=1
	for column in crates:
		column[:] = [x for x in column if x != ' ']
	for line in Lines:
		if "move" not in line:
			continue
		elif "move" in line and line.strip():
			instruction = line.split()
			for count in range(int(instruction[1])):
				crates[int(instruction[5])-1].append(crates[int(instruction[3])-1].pop())
	result = []
	for column in crates:
		result.append(column[-1])
	return ''.join(result)
def part_two(file):
	input = open(file, 'r')
	Lines = input.readlines()
 
	crate_lines = []
	 
	for line in Lines:
		if line.strip():
			crate_lines.append(line)
		else:
			break
	number_of_stacks = len(crate_lines[-1].strip().split())
	crate_lines = crate_lines[:-1]
	layer = 0
	crates = [['' for x in range(number_of_stacks-1)] for y in range(len(crate_lines)+1)]
	for i in range(len(crate_lines)-1, -1, -1):
		for j in range(1, number_of_stacks+1):
			try:
				crate_contents = crate_lines[i][4*j-3]
				crates[j-1][layer] = crate_contents
			except IndexError:
				pass
		layer +=1
	for column in crates:
		column[:] = [x for x in column if x != ' ']
	for line in Lines:
		if "move" not in line:
			continue
		elif "move" in line and line.strip():
			instruction = line.split()
			selection = -1 * int(instruction[1])
			pickup = crates[int(instruction[3])-1][selection:]
			crates[int(instruction[5])-1].extend(pickup)
			crates[int(instruction[3])-1] = crates[int(instruction[3])-1][:-int(instruction[1])]
	result = []
	for column in crates:
		result.append(column[-1])
	return ''.join(result)

if __name__ == '__main__':
	print(part_one('input.txt'))
	print(part_two('input.txt'))