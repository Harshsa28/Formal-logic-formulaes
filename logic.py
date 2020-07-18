class Tree:
    def __init__(self, left, right=None):
        if right == None:
            self.left = left
        else:
            self.left = left
            self.right = righ


class variable:
	def __init__(self):
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

def disjunction:
	def __init__(self, left, right):
		self.left = left
		self.right = right

def implies:
	def __init__(self, left, right):
		self.left = left
		self.right = right



def var(tree, num): #tree is an instance of Tree; num is till which variable I have reached. 9 means I have reached p9
	return "p"+str(num+1)

def not():
	return "not"

def and():
	return "and"

def or():
	return "or"

def implies():
	return "implies"

hades = []


