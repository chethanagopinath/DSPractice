#Find intersection of two lists
#Check how to pass input
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

	def intersection(self, list2):

		p = self.head
		q = list2.head
		l1length = 0
		l2length = 0

		while p.next:
			p = p.next
			l1length += 1

		tail1 = p.data
		l1length += 1	

		while q.next:
			q = q.next
			l2length += 1

		tail2 = q.data
		l2length += 1

		if tail1 != tail2:
			print("There is no intersection")
			return 

		shorter = linkedlist1 if l1length < l2length else linkedlist2
		longer = linkedlist1 if l1length > l2length else linkedlist1

		diff = abs(l1length - l2length)

		p = longer.head

		for i in range(diff):
			p = p.next
			
		q = shorter.head
		
		while p.next is not q:
			p = p.next
			q = q.next
			print(p.data)

linkedlist1 = LinkedList()
linkedlist1.append("3")
linkedlist1.append("1")
linkedlist1.append("5")
linkedlist1.append("9")
linkedlist1.append("7")
linkedlist1.append("2")
linkedlist1.append("1")

linkedlist2 = LinkedList()
linkedlist2.append("4")
linkedlist2.append("6")
linkedlist2.append(linkedlist1.head.next.next.next.next)
linkedlist2.append(linkedlist1.head.next.next.next.next.next)
linkedlist2.append(linkedlist1.head.next.next.next.next.next.next)
print(linkedlist1.head.next.next.next.next.next.next.data)

linkedlist1.intersection(linkedlist2)
