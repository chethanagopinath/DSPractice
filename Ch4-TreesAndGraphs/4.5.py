class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class BinaryTree:
	def __init__(self, root):
		self.root = Node(root)

	def inorder(self):
		if self.root:
			self._inorder(self.root)

	def _inorder(self, curr):
		if curr:
			#no return statement here as you need to traverse the entire tree
			self._inorder(curr.left)
			print(str(curr.data))
			self._inorder(curr.right)

	def bst_satisfied(self):
		if self.root:
			#pass in the root and data of the root and continuously update 
			#these two as we traverse through the tree
			is_satisfied = self._bst_satisfied(self.root, self.root.data)
			#that is, if is_satisfied is not set to False, set it to True
			#we only return False when there is a violation of BST property
			if is_satisfied is None:
				return True
			return False
		return True #even if root node is None, that tree would qualify as a BST

	def _bst_satisfied(self, curr, curr_data):
		if curr.left:
			if curr_data > curr.left.data:
				#you are calling return here as you are assigning this to a var?
				return self._bst_satisfied(curr.left, curr.left.data)
			else:
				return False
		if curr.right:
			if curr_data < curr.right.data:
				return self._bst_satisfied(curr.right, curr.right.data)



#if the data of the root greater than the left child of the root -> not a violation, keep traversing
#else -> violation, return false

tree = BinaryTree(1)
#tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
#print(tree.inorder())
print(tree.bst_satisfied())