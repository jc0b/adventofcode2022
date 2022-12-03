def part_one(file):
	input = open(file, 'r')
	Lines = input.readlines()
	alphabet = list(map(chr, range(ord('a'), ord('z')+1))) + list(map(chr, range(ord('A'), ord('Z')+1)))
	common = []
	scores = []
	for line in Lines:
		bag1 = set(line.strip()[:int(len(line)/2)])
		bag2 = set(line.strip()[int(len(line)/2):])
		common += list(bag1.intersection(bag2))

	for item in common:
		scores.append(alphabet.index(item)+1)
	return sum(scores)

def part_two(file):
	input = open(file, 'r')
	Lines = input.readlines()
	alphabet = list(map(chr, range(ord('a'), ord('z')+1))) + list(map(chr, range(ord('A'), ord('Z')+1)))
	common = []
	scores = []
	for i in range(0, len(Lines), 3):
		elf1 = set(Lines[i].strip())
		elf2 = set(Lines[i+1].strip())
		elf3 = set(Lines[i+2].strip())
		common += list(elf1.intersection(elf2, elf3))

	for item in common:
		scores.append(alphabet.index(item)+1)
	return sum(scores)

if __name__ == '__main__':
	print(part_one('input.txt'))
	print(part_two('input.txt'))