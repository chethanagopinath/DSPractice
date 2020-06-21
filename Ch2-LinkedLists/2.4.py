#Partition a list based on x

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def print_list(self):
		current_node = self.head

		while current_node:
			print(current_node.data)
			current_node = current_node.next

	def append(self, data):
		new_node = Node(data)

		if self.head is None:
			self.head = new_node
			return

		last_node = self.head

		while last_node.next:
			last_node = last_node.next

		last_node.next = new_node

	def partition(self, x):
		#3->5->8->5->10->2->1 (partition = 5)
		#3->1->2->10->5->5->8 (partitioned list)

		p = self.head
		q = self.head
		i = 0
		prev = []

		while q:
			prev.append(q.data)
			i += 1
			q = q.next

		print(prev)

linkedlist = LinkedList()
linkedlist.append("3")
linkedlist.append("5")
linkedlist.append("8")
linkedlist.append("5")
linkedlist.append("10")
linkedlist.append("2")
linkedlist.append("1")

linkedlist.partition(linkedlist.head.next)

