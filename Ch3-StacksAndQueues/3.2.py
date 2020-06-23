class Stack:
	def __init__(self):
		self.items =[]
		self.min_items = []

	def is_empty(self):
		return self.items == []

	def peek_min_stack(self):
		if not self.is_empty():
			return self.min_items[-1]

	def min(self):
		if self.is_empty():
			raise ValueError("Stack is empty!")
		return self.peek_min_stack()

	def push(self, val):
		if self.is_empty():
			self.min_items.append(val)
		else:
			self.min_items.append(min(self.peek_min_stack(), val))
		self.items.append(val)

	def pop(self):
		if self.is_empty():
			raise ValueError("Stack is empty!")
		return self.items.pop()

	def get_stack(self):
		return self.items

stk = Stack()
stk.push(3)
stk.push(1)
print(stk.get_stack())
print(stk.min())


