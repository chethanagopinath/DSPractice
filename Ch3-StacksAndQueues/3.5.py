# #push, pop, peek, is_empty

# class Stack:
# 	def __init__(self):
# 		self.s = []
# 		self.r = []

# 	def is_empty(self, stknum):
# 		if stknum == 1:
# 			return self.s == []
# 		elif stknum == 2:
# 			return self.r == []

# 	def peek(self, stknum):
# 		if stknum == 1:
# 			return self.s[-1]
# 		elif stknum == 2:
# 			return self.r[-1]

# 	def push(self, item, stknum):
# 		if stknum == 1:
# 			self.s.append(item)
# 		elif stknum == 2:
# 			self.r.append(item)

# 	def pop(self, stknum):
# 		if stknum == 1:
# 			return self.s.pop()
# 		elif stknum == 2:
# 			return self.r.pop()

# 	def print_stack(self, stknum):
# 		if stknum == 1:
# 			return self.s
# 		elif stknum == 2:
# 			return self.r
 
# 	def sort_stack(self):
# 		while not self.is_empty(1):
# 			tmp = self.pop(1)
# 			while(!self.is_empty(2) and self.peek(2) > tmp):
# WRONG APPROACH ABOVE!


class Stack:
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()
	
	def is_empty(self):
		return self.items == []

	def peek(self):
		if not self.is_empty():
			return self.items[-1]

	def get_stack(self):
		return self.items

class SortStack:
	def __init__(self, stack_obj):
		self.r = Stack()
		self.s = stack_obj

	def sort_stack(self):
		while not self.s.is_empty():
			tmp = self.s.pop()
			while not self.r.is_empty() and self.r.peek() > tmp:
				self.s.push(self.r.pop())
			self.r.push(tmp)

		while not self.r.is_empty():
			self.s.push(self.r.pop())

	def get_sorted_stack(self):
		if not self.s.is_empty():
			return self.s.get_stack()


stack = Stack()
stack.push(7)
stack.push(6)
stack.push(15)
stack.push(1)
print(stack.get_stack())
sort_obj = SortStack(stack)
sort_obj.sort_stack()
print(sort_obj.get_sorted_stack())




