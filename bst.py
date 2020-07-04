class Node:
	def __init__(self, data=None):
		self.data = data
		self.left = None
		self.right = None

class BST:
	def __init__(self, root):
		self.root = None

	def insert(self, data):
		if self.root is None:
			self.root = Node(data)
		else:
			#helper function that checks if self.root(the current node) at every iteration is greater
			#than the value to be inserted or not 
			#then it inserts into true at the appropriate position
			self._insert(data, self.root)

	def _insert(self, data, curr):
		if data < curr.data:
			if curr.left is None:
				curr.left = Node(data)
			else:
				self._insert(data, curr.left)
		elif data > curr.data:
			if curr.right is None:
				curr.right = Node(data)
			else:
				self._insert(data, curr.right)
		else:
			print("Value already present in tree")

	def find(self, data):
		if self.root:
			#set is found to either true or false
			#this evaluation is done by the helper method which traverses 
			#through the tree and figures out whether true or false
			found = self._find(data, self.root)
			if found:
				return True
			return False
		else:
			return None

	def _find(self, data, curr):
		if data < curr.data and curr.left:
			#if lesser than data and current.left exists, recursively keep going left
			#setting curr.left as root and traverse till you reach
			#data == curr.left
			return self._find(data, curr.left)
		elif data > curr.data and curr.right:
			return self._find(data, curr.right)
		if data == curr.data:
			return True
bst = BST()
bst.insert(8)
bst.insert(7)
bst.insert(9)
bst.insert(1)
print(bst.find(9))
print(bst.find(2))

