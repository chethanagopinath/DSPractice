#Create linked list
#Append to linked list

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
		while last_node.next:
			last_node = last_node.next
		#When loop breaks, set the last_node's next to the new_node
		last_node.next = new_node

	def prepend(self, data):
		#first create node
		new_node = Node(data)
		#point the inserted node's next to the current head
		new_node.next = self.head
		#make the inserted node as the list's new head
		self.head = new_node
		
		#A->B->C->D  E
		#E->A->B->C->D

	def insert_after_node(self, data, prev_node):
		if not prev_node:
			print("Cannot insert as given previous node not in list")
			return 
		#Create node
		new_node = Node(data)
		#A->B->C->D
		#A->B->E->C->D
		new_node.next = prev_node.next
		prev_node.next = new_node

	def delete_node(self, key):
		#Two cases - 1) Node to be deleted is the head of the list
		#2) Node to be deleted is wedged in between other nodes

		#A->B->C->D->E
		#B->C->D->E
		current_node = self.head

		#when element to be deleted is the head of the list
		if current_node and current_node.data == key:
			self.head = current_node.next
			current_node = None
			return

		#if element to be deleted is wedged between two nodes
		#we should know both prev node and next node of the current node(node to be deleted)
		#make previous' next point to current's next
		#A->B->C->D, B is the node to be deleted

		prev = None

		#loop till you reach the current node as node before the key to be deleted
		#From the previous example, you would be at A
		#Then set prev 
		while current_node and current_node.data != key:
			prev = current_node
			current_node = current_node.next

		if current_node is None:
			print("Element is not present in list")
			return 

		prev.next = current_node.next
		current_node = None

	def delete_node_by_position(self, pos):
		#Two cases - 1) Node to be deleted is the head of the list
		#2) Node to be deleted is wedged in between other nodes

		current_node = self.head
		pos_list = 0
		#in the video, pos_list is set later on
		#current_node and 
		if current_node and pos_list == pos:
		#if pos_list == 0:
			self.head = current_node.next
			current_node = None
			return

		prev = None
		#while current_node means while we could continue to go through the linked list
		while current_node and pos_list != pos:
			prev = current_node
			current_node = current_node.next
			pos_list += 1

		if current_node is None:
			return

		prev.next = current_node.next
		current_node = None 

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

	def len_recursive(self, node):
		if node is None:
			return 0
		return 1 + self.len_recursive(node.next)
		#start from node = self.head(send the head when you call this function) and then 
		#add 1 and traverse to the next node



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
#linkedlist.insert_after_node("E", linkedlist.head.next.next.next)
#print(linkedlist.head.next.next.data)
#linkedlist.delete_node("B")
#linkedlist.delete_node_by_position(2)
linkedlist.remove_duplicates()
print(linkedlist.len_recursive(linkedlist.head))

linkedlist.print_list()