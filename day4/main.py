def part_one(file):
	input = open(file, 'r')
	Lines = input.readlines()
	common = []
	for line in Lines:
		elf1, elf2 = line.strip().split(',')
		
		elf1 = elf1.split('-')
		elf1_range = list(range(int(elf1[0]), int(elf1[1])+1))
		elf2 = elf2.split('-')
		elf2_range = list(range(int(elf2[0]), int(elf2[1])+1))

		if all(x in elf1_range for x in elf2_range) or all(x in elf2_range for x in elf1_range):
			common.append(elf1_range)

	return len(common)

def part_two(file):
	input = open(file, 'r')
	Lines = input.readlines()
	common = []
	for line in Lines:
		elf1, elf2 = line.strip().split(',')
		
		elf1 = elf1.split('-')
		elf1_range = set(list(range(int(elf1[0]), int(elf1[1])+1)))
		elf2 = elf2.split('-')
		elf2_range = set(list(range(int(elf2[0]), int(elf2[1])+1)))

		if len(list(elf1_range.intersection(elf2_range))) > 0:
			common.append(elf1_range)

	return len(common)

if __name__ == '__main__':
	print(part_one('input.txt'))
	print(part_two('input.txt'))