#Sum of two lists
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


	def sum_lists(self, list2):
		p = self.head
		q = list2.head

		sum_list = LinkedList()
		carry = 0
		while p or q:
			if not p:
				i = 0
			else:
				i = p.data
			if not q:
				j = 0
			else:
				j = q.data
			s = i + j + carry

			#As you are adding just two lists, the max could be 9 + 9 = 18, with carry 1
			#If s is greater than 10, compute remainder and append it, the carry would get added in the next iteration
			#Except for the last carry which is dealt with after the loop
			if s >= 10:
				carry = 1
				remainder = s % 10
				sum_list.append(remainder)
			else:
				carry = 0
				sum_list.append(s)

			if p:
				p = p.next
			if q:
				q = q.next

		if carry != 0:
			sum_list.append(carry)

		sum_list.print_list()

linkedlist1 = LinkedList()
linkedlist1.append(5)
linkedlist1.append(6)
linkedlist1.append(3)

linkedlist2 = LinkedList()
linkedlist2.append(4)
linkedlist2.append(8)
linkedlist2.append(9)

#3 6 5
#9 8 4
#-----
#13 4 9

#Carry is appended to the sum_list after loop - do not forget

print(365 + 984)
linkedlist1.sum_lists(linkedlist2)




		