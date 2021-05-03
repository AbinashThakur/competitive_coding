class Node:
	def __init__(self):
		self.data = 0
		self.next = None

def newNode(data):

	new_node = Node()
	new_node.data = data
	new_node.next = None
	return new_node

def partition(head, x) :
	smallerHead = None
	smallerLast = None
	greaterLast = None
	greaterHead = None
	equalHead = None
	equalLast = None

	while (head != None) :
	
		if (head.data == x):
		
			if (equalHead == None):
				equalHead = equalLast = head
			else:
			
				equalLast.next = head
				equalLast = equalLast.next
			
		elif (head.data < x):
		
			if (smallerHead == None):
				smallerLast = smallerHead = head
			else:
			
				smallerLast.next = head
				smallerLast = head
		
		else :
		
			if (greaterHead == None) :
				greaterLast = greaterHead = head
			else:
			
				greaterLast.next = head
				greaterLast = head
			
		head = head.next
	
	if (greaterLast != None) :
		greaterLast.next = None

	if (smallerHead == None) :
	
		if (equalHead == None) :
			return greaterHead
		equalLast.next = greaterHead
		return equalHead
	
	if (equalHead == None) :
	
		smallerLast.next = greaterHead
		return smallerHead
	
	smallerLast.next = equalHead
	equalLast.next = greaterHead
	return smallerHead

def printList(head) :

	temp = head
	while (temp != None):
	
		print(temp.data ,end= " ")
		temp = temp.next
	

head = newNode(10)
head.next = newNode(4)
head.next.next = newNode(5)
head.next.next.next = newNode(30)
head.next.next.next.next = newNode(2)
head.next.next.next.next.next = newNode(50)

x = 3
head = partition(head, x)
printList(head)