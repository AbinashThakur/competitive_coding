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

	def removeDup(self, start):
		if self.start == None or self.start.next == None:
			return self.start
		
		str_dup = set()
		temp = start
		str_dup.add(self.start.data)
		while temp.next is not None:
		    if temp.next.data in str_dup:
		        temp.next = temp.next.next
		    else:
		        str_dup.add(temp.next.data)
		        temp = temp.next
		
		return self.start

if __name__ == "__main__":
    llist = LinkedList()
    llist.start = Node(10)
    second = Node(12)
    third = Node(11)
    fourth = Node(11)
    fifth = Node(12)
    sixth = Node(11)
    seventh = Node(10)

    llist.start.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    sixth.next = seventh

    print("Linked List before removing Duplicates.")
    llist.printlist()
    llist.removeDup(llist.start)
    print("\nLinked List after removing duplicates.")
    llist.printlist()