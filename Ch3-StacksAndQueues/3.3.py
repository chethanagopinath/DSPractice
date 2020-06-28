class Stack:
	def __init__(self, capacity):
		self.stacks = []
		if capacity < 1:
			raise NameError("Capacity should be greater than 1")
		else:
			self.capacity = capacity

	def is_empty(self):
		return self.stacks == []

	def push(self, item):
		if self.is_empty():
			self.stacks.append([item])
		else:
			if len(self.stacks[-1]) >= self.capacity:
				self.stacks.append([item])
			else:
				self.stacks[-1].append(item)

	def pop(self):
		if self.is_empty():
			raise NameError("Can't pop from empty stack")
		else:
			popped = self.stacks[-1][-1]
			if len(self.stacks[-1]) == 1:
				del self.stacks[-1]
			else:
				del self.stacks[-1][-1]

			return popped

	def popAt(self, index):
		if self.is_empty():
			raise NameError("Can't pop from empty stack")

		elif index-1 > len(self.stacks):
			raise NameError("Index is out of range")

		else:
			#This pops the last element in selected index of main stack
			popped = self.stacks[index-1][-1] 

			if len(self.stacks[index-1]) == 1:
				del self.stacks[-1]
				#in case of desired index stack having just one element, delete the stack
			elif len(self.stacks) == index: 
				#that is, if the index indicates the last stack in list of stacks
				del self.stacks[-1][-1]
			else:
				#if the index is some stack in between in the list of stacks
				self.stacks[index-1][-1] = self.stacks[index][0]
				#[[1,2,3,4], [5,6,7,8], [9,10]]
				#Popping at some index means, popping the last element of 
				#the required stack based on index
				#If index = 2
				#Pop 10 from last stack of the main stack
				#If index = 1
				#Pop 8 from second stack of main stack
				#You must then bring 9 from last stack to this stack
				#Move up one element
				for i in range(index, len(self.stacks)):
					#i in range of 1 to 3
					for j in range(0, len(self.stacks[i])-1):
						#j in range of 0 to 3 ([5,6,7,8])
						self.stacks[i][j] = self.stacks[i][j+1]
						#move by one element, pushing jth element by one space
						#pushing last element of second last stack to last stack
						if i < len(self.stacks)-1:
							self.stacks[i][-1] = self.stacks[i+1][0]

				del self.stacks[-1][-1]

				#if stack is empty, delete it
				if len(self.stacks[-1]) == 0:
					del self.stacks[-1] 
			return popped

	def get_stack(self):
		if not self.is_empty():
			return self.stacks

stack = Stack(3)
stack.push(11)
stack.push(22)
stack.push(33)
stack.push(44)
stack.push(55)
stack.push(66)
stack.push(77)
stack.push(88)
#[[11,22,33], [44,55,66], [77,88]]
print(stack.popAt(2))
#[[11,22,33], [44,55,77], [88]]
print(stack.get_stack())
