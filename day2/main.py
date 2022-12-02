def part_one(file):
	input = open(file, 'r')
	Lines = input.readlines()
	
	winning_plays = [['A', 'B'], ['B', 'C'], ['C', 'A']]
	scores = []
	for line in Lines:
		score = 0
		play = line.replace('X', 'A').replace('Y', 'B').replace('Z', 'C').split()
		if play[1] == 'A':
			score+=1
		elif play[1] == 'B':
			score+=2
		elif play[1] == 'C':
			score+=3
		if play in winning_plays:
			score +=6
		elif play[0] == play[1]:
			score+=3
		scores.append(score)
	return sum(scores)


def part_two(file):
	win = {
		'A': 8,
		'B': 9,
		'C': 7
	}

	draw = {
		'A': 4,
		'B': 5,
		'C': 6
	}

	lose = {
		'A': 3,
		'B': 1,
		'C': 2
	}
	input = open(file, 'r')
	Lines = input.readlines()

	scores = []
	for line in Lines:
		score = 0
		play = line.split()
		if play[1] == 'X':
			score = lose[play[0]]
		elif play[1] == 'Y':
			score = draw[play[0]]
		elif play[1] == 'Z':
			score = win[play[0]]
		scores.append(score)
	return sum(scores)

if __name__ == '__main__':
	print(part_one('input.txt'))
	print(part_two('input.txt'))