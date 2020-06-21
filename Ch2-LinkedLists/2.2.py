#nth to last node
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
		#if list is empty/for adding the first element
		if self.head is None:
			self.head = new_node
			return
		#else, what should be done?
		#set the last_node to be head(last_node as eventually you are going to add the new_node 
		#after the last_node of the list)

		last_node = self.head
		#iterate till last node
		while last_node.next:
			last_node = last_node.next

		#when the loop reaches the last_node, add new_node as last_node's next
		last_node.next = new_node

	def len_iterative(self):
		current_node = self.head
		length = 0

		while current_node:
			current_node = current_node.next
			length += 1

		return length

	def nth_to_last_node(self, n):
		#A->B->C->D->E
		
		length = self.len_iterative()
		nth_node = self.head
		# while length != n:
		# 	nth_node = nth_node.next
		# 	length -= 1
		# return nth_node.data

		while nth_node:
			if length == n:
				return nth_node.data
			else:
				length -= 1
			nth_node = nth_node.next 

		if nth_node is None:
			return
	
	def nth_to_last_node_runners(self, n):
		p = self.head
		q = self.head
		count = 0
		#make q point to nth node
		while q and count < n:
			q = q.next
			count += 1

		if not q:
			print(str(n) + "is greater than number of nodes in list.")
			return 
		#now move both p and q until q reaches null
		while p and q:
			p = p.next
			q = q.next

		return p.data







linkedlist = LinkedList()
linkedlist.append("A")
linkedlist.append("B")
linkedlist.append("C")
linkedlist.append("D")
linkedlist.append("E")

#print(linkedlist.nth_to_last_node(3))
print(linkedlist.nth_to_last_node_runners(3))



