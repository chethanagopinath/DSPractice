class MyQueue:
	#enqueue into stack1
	#add from stack1 to stack2, so the order of the items are reversed
	#now pop the top from stack2
	def __init__(self):
		self.stack1 = []
		self.stack2 = []	

	def enqueue(self, item):
		self.stack1.append(item)


	#Can write a get_size method too, also a peek method

	def get_queue(self):
		if len(self.stack1) != 0:
			return self.stack1[::-1]
		return self.stack2

	def dequeue(self):
		#if len(stack2) = 0, pop elements from stack1 and push to stack2 until len(stack1) > 0
		#if len(stack2) is not 0, return popped element stored from while loop

		if len(self.stack2) == 0:

			if len(self.stack1) == 0:
				raise NameError("Cannot dequeue from empty queue")
			else:
				while(len(self.stack1)>0):
					element = self.stack1.pop()
					self.stack2.append(element)

		return self.stack2.pop()

queue = MyQueue()
queue.enqueue(5)
queue.enqueue(3)
queue.enqueue(10)
print(queue.get_queue())
print(queue.dequeue())
print(queue.get_queue())





		