#Create linked list
#Append to linked list
#remove duplicates

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
		#Pass the value to be inserted as data
		new_node = Node(data)

		if self.head is None:
			self.head = new_node
			return

		last_node = self.head
		#iterate till the last node and then add new_node as last_node's next
		while last_node.next:
			last_node = last_node.next
		#When loop breaks, set the last_node's next to the new_node
		last_node.next = new_node

	def remove_duplicates(self):
		current_node = self.head
		prev = None

		duplicates = dict()

		while current_node:
			if current_node.data in duplicates:
				#In 1->2->1 example, prev.data = 2, set prev.next to current.next 
				#Then set current node to None to remove the current node
				prev.next = current_node.next
				current_node = None
			else:
				duplicates[current_node.data] = 1
				#remember to set a value for prev, normal flow of a linked list
				prev = current_node
			current_node = prev.next


linkedlist = LinkedList()
linkedlist.append("A")
linkedlist.append("B")
linkedlist.append("C")
linkedlist.append("D")
linkedlist.append("C")
linkedlist.append("A")
linkedlist.append("B")
linkedlist.append("C")
linkedlist.append("E")
linkedlist.append("C")
linkedlist.append("A")

linkedlist.remove_duplicates()

linkedlist.print_list()