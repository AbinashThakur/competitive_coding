class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.start = None

	def printlist(self):
		temp = self.start
		while temp!=None:
			print(temp.data)
			temp = temp.next

	def DeleteMid(self):

		if self.start is None or self.start.next is None:
			return
		
		fast_ptr = self.start
		slow_ptr = self.start
		prev_ptr = None
		
		while fast_ptr is not None and fast_ptr.next is not None:
			fast_ptr = fast_ptr.next.next
			prev_ptr = slow_ptr
			slow_ptr = slow_ptr.next
		
		prev_ptr.next = slow_ptr.next

		return self.start

if __name__ == "__main__":
	llist = LinkedList()
	llist.start = Node(20)
	second = Node(4)
	third = Node(15)
	fourth = Node(35)

	llist.start.next = second
	second.next = third
	third.next = fourth

	print("Before Delete:")
	llist.printlist()
	llist.DeleteMid()
	print("After Delete:")
	llist.printlist()