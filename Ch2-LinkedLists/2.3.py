#Delete middle node
class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None


	def print_linkedlist(self):
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

	def delete_middle_node_given_head(self, key):
		#A->B->C->D->E->F, Given node = C

		current_node = self.head
		prev = None

		while current_node and current_node.data != key:
			prev = current_node
			current_node = current_node.next

		if current_node is None:
			print("Element not present in list")
			return

		prev.next = current_node.next
		current_node = None

	def delete_middle_node(self, node):
		#When head of list is not given
		if node is None or node.next is None:
			print("Node is not present in list")
		#Take the node, copy over the data and next part of the next node to node
		next_node = node.next
		#print(type(next_node))

		node.data = next_node.data
		node.next = next_node.next
		return True

linkedlist = LinkedList()  
linkedlist.append("A")
linkedlist.append("B")
linkedlist.append("C")
linkedlist.append("D")
#print(linkedlist.head.next.next)

linkedlist.delete_middle_node(linkedlist.head.next)

linkedlist.print_linkedlist()



