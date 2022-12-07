def part_one(file):
	input = open(file, 'r')
	Lines = input.readlines()
	
	cursor = None
	root_element = None
	for line in Lines:
		parsing_line = line.strip().split()
		if parsing_line[0] == "$" and parsing_line[1] == "cd":
			if cursor is None and parsing_line[2] != "..":
				cursor = ElfFile(name=parsing_line[2], parent=cursor)
				root_element = cursor
			elif parsing_line[2] == "..":
				cursor = cursor.get_parent()
			else:
				cursor = cursor.get_child(parsing_line[2])
		elif parsing_line[0] == "dir":
			new_child = ElfFile(name=parsing_line[1], parent=cursor)
			cursor.add_child(new_child)
			new_child.set_parent(cursor)
		elif parsing_line[0] == "$" and parsing_line[1] == "ls":
			continue
		else:
			new_child = ElfFile(name=parsing_line[1], size=parsing_line[0], parent=cursor)
			cursor.add_child(new_child)
	return search(root_element)

def search(file_object):
	if len(file_object.children) <= 0:
		return 0
	else:
		result = 0
		if file_object.file_size <= 100000:
			result = int(file_object.file_size)
		for child in file_object.children:
			result += search(child) 
		return result

def part_two(file):
	input = open(file, 'r')
	Lines = input.readlines()
	FS_SIZE = 70000000
	UPDATE_SIZE = 30000000
	
	cursor = None
	root_element = None
	for line in Lines:
		parsing_line = line.strip().split()
		if parsing_line[0] == "$" and parsing_line[1] == "cd":
			if cursor is None and parsing_line[2] != "..":
				cursor = ElfFile(name=parsing_line[2], parent=cursor)
				root_element = cursor
			elif parsing_line[2] == "..":
				cursor = cursor.get_parent()
			else:
				cursor = cursor.get_child(parsing_line[2])
		elif parsing_line[0] == "dir":
			new_child = ElfFile(name=parsing_line[1], parent=cursor)
			cursor.add_child(new_child)
			new_child.set_parent(cursor)
		elif parsing_line[0] == "$" and parsing_line[1] == "ls":
			continue
		else:
			new_child = ElfFile(name=parsing_line[1], size=parsing_line[0], parent=cursor)
			cursor.add_child(new_child)
	space_free = FS_SIZE - root_element.file_size
	required_space = UPDATE_SIZE - space_free
	directory_sizes = find_all_dir_sizes(root_element)
	suitable_directories = []
	for directory_size in directory_sizes:
		if directory_size >= required_space:
			suitable_directories.append(directory_size)
	suitable_directories.sort()
	return suitable_directories[0]


def find_all_dir_sizes(file_object):
	if len(file_object.children) <= 0:
		return []
	else:
		result = [int(file_object.file_size)]
		for child in file_object.children:
			result += find_all_dir_sizes(child) 
		return result

class ElfFile:
	
	def __init__(self, name, size=0, parent=None):
		self.children = []
		self.file_size = size
		self.file_name = name
		self.parent = parent

	def add_child(self, child_object):
		self.children.append(child_object)
		self.update_size()

	def get_child(self, name):
		for child in self.children:
			if child.file_name == name:
				return child

	def update_size(self):
		self.file_size = sum([int(x.file_size) for x in self.children])
		if self.parent is not None:
			self.parent.update_size()	

	def get_parent(self):
		return self.parent

	def set_parent(self, parent_object):
		self.parent = parent_object



if __name__ == '__main__':
	print(part_one('input.txt'))
	print(part_two('input.txt'))

