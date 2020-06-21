#Palindrome check
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

	def is_palindrome(self):
		#Method 1 - String reverse check
		# p = self.head
		# s = ""
		# while p:
		# 	s += p.data
		# 	p = p.next

		# return s == s[::-1]

		#Method 2 - Using a stack
		# s = []
		# p = self.head
		# while p:
		# 	s.append(p.data)
		# 	p = p.next
		# p = self.head
		
		# while p:
		# 	data = s.pop()
		# 	if data != p.data:
		# 		return False
		# 	p = p.next
		# return True

		#Method 3 - Compare front and tail elements one by one
		p = self.head
		q = self.head

		prev = []
		i = 0
		while q:
			prev.append(q)
			q = q.next
			i += 1

		q = prev[i - 1]
		count = 1

		while count <= i//2 + 1: #checks the number of comparisons, would work without the
		# + 1 too but should account for edge cases, try doing an iteration, you will understand
			if prev[-count].data != p.data:
				return False
			p = p.next 
			count += 1
		return True




linkedlist1 = LinkedList()
linkedlist1.append("R") #--> p
linkedlist1.append("A")
linkedlist1.append("C")
linkedlist1.append("E")
linkedlist1.append("C")
linkedlist1.append("A")
linkedlist1.append("R") #--> q, i = 7
print(linkedlist1.is_palindrome())

linkedlist2 = LinkedList()
linkedlist2.append("A")
linkedlist2.append("R")
linkedlist2.append("T")
print(linkedlist2.is_palindrome())



