def part_one(file):
	input = open(file, 'r')
	Lines = input.readlines()

	head = (0, 0)
	tail = (0, 0)

	tail_locations = set()

	for line in Lines:
		match line.split()[0]:
			case "U":
				for i in range(int(line.split()[1])):
					head = (head[0], head[1]+1)
					tail = process_tail(head, tail)
					tail_locations.add(tail)
			case "D":
				for i in range(int(line.split()[1])):
					head = (head[0], head[1]-1)
					tail = process_tail(head, tail)
					tail_locations.add(tail)
			case "L":
				for i in range(int(line.split()[1])):
					head = (head[0]-1, head[1])
					tail = process_tail(head, tail)
					tail_locations.add(tail)
			case "R":
				for i in range(int(line.split()[1])):
					head = (head[0]+1, head[1])
					tail = process_tail(head, tail)
					tail_locations.add(tail)
			case _:
				print(f"Unknown instruction {line.split()[0]} passed.")
	return(len(tail_locations))

def sign(val):
	if val == 0:
		return 0
	else:
		return val // abs(val)

def process_tail(head, tail):
	if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
		return (tail[0] + sign(head[0] - tail[0]), tail[1] + sign(head[1] - tail[1]))
	else:
		return tail

def part_two(file):
	input = open(file, 'r')
	Lines = input.readlines()
	ROPE_LENGTH = 10
	rope = [(0, 0) for x in range(ROPE_LENGTH)]

	tail_locations = set()

	for line in Lines:
		match line.split()[0]:
			case "U":
				for i in range(int(line.split()[1])):
					rope[0] = (rope[0][0], rope[0][1]+1)
					for i in range(ROPE_LENGTH-1):
						rope[i+1] = process_tail(rope[i], rope[i+1])
					tail_locations.add(rope[-1])
			case "D":
				for i in range(int(line.split()[1])):
					rope[0] = (rope[0][0], rope[0][1]-1)
					for i in range(ROPE_LENGTH-1):
						rope[i+1] = process_tail(rope[i], rope[i+1])
					tail_locations.add(rope[-1])
			case "L":
				for i in range(int(line.split()[1])):
					rope[0] = (rope[0][0]-1, rope[0][1])
					for i in range(ROPE_LENGTH-1):
						rope[i+1] = process_tail(rope[i], rope[i+1])
					tail_locations.add(rope[-1])
			case "R":
				for i in range(int(line.split()[1])):
					rope[0] = (rope[0][0]+1, rope[0][1])
					for i in range(ROPE_LENGTH-1):
						rope[i+1] = process_tail(rope[i], rope[i+1])
					tail_locations.add(rope[-1])
			case _:
				print(f"Unknown instruction {line.split()[0]} passed.")
	return(len(tail_locations))

if __name__ == '__main__':
	print(part_one('input.txt'))
	print(part_two('input.txt'))
