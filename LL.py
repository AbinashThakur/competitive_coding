class node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.start = None

	def insertLast(self, value):
		newNode = node(value)
		if self.start == None:
			self.start = newNode
		else:
			temp = self.start
			while temp.next!=None:
				temp = temp.next
			temp.next = newNode

	def viewList(self):
		if self.start == None:
			print("List is Empty")
		else:
			temp = self.start
			while temp!=None:
				print(temp.data)
				temp = temp.next

	def deleteFirst(self):
		if self.start == None:
			print("List is Empty")
		else:
			self.start = self.start.next


if __name__ == "__main__":
	mylist = LinkedList()
	mylist.insertLast(10)
	mylist.insertLast(20)
	mylist.insertLast(40)
	mylist.viewList()
	mylist.deleteFirst()
	mylist.viewList()

#end

