class variable:
	def __init__(self):
		#self.name = name
		self.left = None
		self.right = None

class negation:
	def __init__(self, left):
		self.left = left
		self.right = None

class conjunction:
	def __init__(self, left, right):
		self.left = left
		self.right = right

class disjunction:
	def __init__(self, left, right):
		self.left = left
		self.right = right

class implies:
	def __init__(self, left, right):
		self.left = left
		self.right = right

def print_tree(tree):
	if isinstance(tree, variable):
		return "p"
	if isinstance(tree, negation):
		return "(~"+print_tree(tree.left)+")"
	if isinstance(tree, conjunction):
		return "("+print_tree(tree.left)+" /\ "+print_tree(tree.right)+")"
	if isinstance(tree, disjunction):
		return "("+print_tree(tree.left)+" \/ "+print_tree(tree.right)+")"
	if isinstance(tree, implies):
		return "("+print_tree(tree.left)+" -> "+print_tree(tree.right)+")"

def print_levels(levels):
	for i in levels:
		for j in i:
			print(print_tree(j))
		print('*'*500)

def make():
	levels = [[] for i in range(4)]
	levels[0].append(variable())
	for i in range(1, 4):
		levels[i].append(variable())
		for j in levels[i-1]:
			levels[i].append(negation(j))
		for j in levels[i-1]:
			for k in levels[i-1]:
				levels[i].append(conjunction(j,k))
				levels[i].append(disjunction(j,k))
				levels[i].append(implies(j,k))
	print_levels(levels)
	print(len(levels[0]))
	print(len(levels[1]))
	print(len(levels[2]))
	print(len(levels[3]))


make()

