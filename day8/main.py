def part_one(file):
	input = open(file, 'r')
	Lines = input.readlines()
 
	forest = []
	 
	for line in Lines:
		forest.append([int(tree) for tree in line.strip()])

	unsuitable = []
	for i in range(len(forest)):
		for j in range(len(forest[i])):
			if (i == 0 or i == len(forest)-1):
				unsuitable.append(forest[i][j])
				continue
			elif (j == 0 or j == len(forest[i])-1):
				unsuitable.append(forest[i][j])
				continue
			else:
				column = [forest[l][j] for l in range(len(forest[i]))]
				if all(m < forest[i][j] for m in column[:i]) or all(m < forest[i][j] for m in column[i+1:]) or all(m < forest[i][j] for m in forest[i][:j]) or all(m < forest[i][j] for m in forest[i][j+1:]):
					unsuitable.append(forest[i][j])
	return len(unsuitable)

def part_two(file):
	input = open(file, 'r')
	Lines = input.readlines()
 
	forest = []
	 
	for line in Lines:
		forest.append([int(tree) for tree in line.strip()])
	scores = []
	unsuitable = []
	for i in range(len(forest)):
		for j in range(len(forest[i])):
			column = [forest[l][j] for l in range(len(forest[i]))]

			going_north = column[:i]
			going_north.reverse()
			distances = []
			if len(going_north) > 0:
				for h in range(forest[i][j], 10):
					if h in going_north:
						distance = going_north.index(h)+1
						distances.append(going_north.index(h)+1)
				distances.sort()
				if len(distances) == 0:
					north_score = len(going_north)
				else:
					north_score = distances[0]
			else:
				north_score = 0
			
			distances = []
			if len(column[i+1:]) > 0:
				for t in range(forest[i][j], 10):
					if t in column[i+1:]:
						distance = column[i+1:].index(t)+1
						distances.append(column[i+1:].index(t)+1)
				distances.sort()
				if len(distances) == 0:
					south_score = len(column[i+1:])
				else:
					south_score = distances[0]
			else:
				south_score = 0
			
			distances = []
			if len(forest[i][j+1:]) > 0:
				for t in range(forest[i][j], 10):
					if t in forest[i][j+1:]:
						distance = forest[i][j+1:].index(t)+1
						distances.append(forest[i][j+1:].index(t)+1)
				distances.sort()
				if len(distances) == 0:
					east_score = len(forest[i][j+1:])
				else:
					east_score = distances[0]
			else:
				east_score = 0

			going_west = forest[i][:j]
			going_west.reverse()
			distances = []
			if len(going_west) > 0:
				for t in range(forest[i][j], 10):
					if t in going_west:
						distance = going_west.index(t)+1
						distances.append(going_west.index(t)+1)
				distances.sort()
				if len(distances) == 0:
					west_score = len(going_west)
				else:
					west_score = distances[0]
			else:
				west_score = 0

			total_score = north_score * south_score * east_score * west_score			
			scores.append(total_score)
	scores.sort(reverse=True)
	return scores[0]

if __name__ == '__main__':
	print(part_one('input.txt'))
	print(part_two('input.txt'))