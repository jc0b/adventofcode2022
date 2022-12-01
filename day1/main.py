def part_one(file):
	input = open(file, 'r')
	Lines = input.readlines()
 
	current_sum = 0
	elves = []
	for line in Lines:
		if line.strip():
			current_sum+=int(line)
		else:
			elves.append(current_sum)
			current_sum=0
	elves.sort(reverse=True)
	return(elves[0])

def part_two(file):
	input = open(file, 'r')
	Lines = input.readlines()
 
	current_sum = 0
	elves = []
	for line in Lines:
		if line.strip():
			current_sum+=int(line)
		else:
			elves.append(current_sum)
			current_sum=0
	elves.sort(reverse=True)
	return(elves[0] + elves[1] + elves[2])

if __name__ == '__main__':
	print(part_one('input.txt'))
	print(part_two('input.txt'))