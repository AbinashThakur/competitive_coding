class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.start = None

	def printNthFromLast(self, n):
		main_ptr = self.start
		ref_ptr = self.start

		count = 0
		if self.start is not None:
			while count<n:
				if ref_ptr is None:
					print ("%d is greater than the no. pf nodes in list" % n)
					return
				ref_ptr = ref_ptr.next
				count +=1
		
		while ref_ptr is not None:
			main_ptr = main_ptr.next
			ref_ptr = ref_ptr.next

		print ("Node no. %d from last is %d" % (n, main_ptr.data))

if __name__ == "__main__":
	llist = LinkedList()
	llist.start = Node(20)
	second = Node(4)
	third = Node(15)
	fourth = Node(35)

	llist.start.next = second
	second.next = third
	third.next = fourth

	llist.printNthFromLast(4)