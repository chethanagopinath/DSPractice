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

stack = Stack()
print(stack.is_empty())
stack.push("1")
stack.push("3")
stack.push("5")
stack.push("7")
stack.push("9")
stack.push("11")
print(stack.get_stack())
stack.pop()
print(stack.get_stack())
print(stack.peek())
