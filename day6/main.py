def part_one(file):
	input = open(file, 'r')
	Lines = input.readlines()
 
	for line in Lines:
 		for i in range(len(line)-4):
 			sample = set(line[i:i+4])
 			if len(sample) == 4:
 				return i+4

def part_two(file):
	input = open(file, 'r')
	Lines = input.readlines()
 
	for line in Lines:
 		for i in range(len(line)-14):
 			sample = set(line[i:i+14])
 			if len(sample) == 14:
 				return i+14

if __name__ == '__main__':
	print(part_one('input.txt'))
	print(part_two('input.txt'))