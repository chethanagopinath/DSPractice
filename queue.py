class Queue:
	def __init__(self):
		self.items = []

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		return self.items.pop()

	def is_empty(self):
		return self.items == []

	def size(self):
		return len(self.items)

	def peek(self):
		if not self.is_empty():
			return self.items[-1]

	def get_queue(self):
		return self.items[::-1]

queue = Queue()
print(queue.is_empty())
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")
print(queue.peek())
#print(queue.get_queue())
queue.dequeue()
#print(queue.get_queue())
print(queue.peek())