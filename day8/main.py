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
				# print("---------------")
				# print(f"Line: {forest[i]}")
				# print(f"Index i: {i}: range = {len(forest)}")
				# print(f"Index j: {j}: range = {len(forest[i])}")
				# print(f"North of {forest[i][j]}: {column[:i]}")
				# print(f"South of {forest[i][j]}: {column[i+1:]}")
				# print(f"East of {forest[i][j]}: {forest[i][:j]}")
				# print(f"West of {forest[i][j]}: {forest[i][j+1:]}")
				# print("---------------")
				if all(m < forest[i][j] for m in column[:i]) or all(m < forest[i][j] for m in column[i+1:]) or all(m < forest[i][j] for m in forest[i][:j]) or all(m < forest[i][j] for m in forest[i][j+1:]):
					unsuitable.append(forest[i][j])
	return len(unsuitable)

def part_two(file):
	pass

if __name__ == '__main__':
	print(part_one('input.txt'))
	print(part_two('input.txt'))