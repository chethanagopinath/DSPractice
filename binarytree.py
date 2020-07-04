class Node:
	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None

class BinaryTree:
	def __init__(self, root):
		self.root = Node(root)

	def print_tree(self, traversal_type):
		if traversal_type == "preorder":
			return self.preorder(self.root, "")
		elif traversal_type == "inorder":
			return self.inorder(self.root, "")
		elif traversal_type == "postorder":
			return self.postorder(self.root, "")
		else:
			raise Exception("Invalid traversal type -> " + str(traversal_type))
			return False

	def preorder(self, start, traversal):
		#Root(start/node in this case) -> Left -> Right
		if start:
			#append value of node to traversal string
			#this is updated continuously for every single recursive call
			traversal += str(start.value) + "->"
			#append left 
			traversal = self.preorder(start.left, traversal)
			#once left subtree is traversed recursively, append right subtree of start
			traversal = self.preorder(start.right, traversal)
		return traversal

	def inorder(self, start, traversal):
		#Natural reading style, left to right, hence the name, inorder
		#Left -> Root -> Right
		if start:
			#left
			traversal = self.inorder(start.left, traversal)
			#print it
			traversal += str(start.value) + "->"
			#right
			traversal = self.inorder(start.right, traversal)
		return traversal

	def postorder(self, start, traversal):
		#Left -> Right -> Root
		if start:
			#left
			traversal = self.postorder(start.left, traversal)
			#right
			traversal = self.postorder(start.right, traversal)
			#root
			traversal += str(start.value) + "->"
		return traversal

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))
print(tree.print_tree("order"))


