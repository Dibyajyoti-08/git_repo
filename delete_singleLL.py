#!/usr/bin/python3

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

def printNode(head):
	currentNode = head
	while currentNode:
		print(currentNode.data, end='->')
		currentNode = currentNode.next
	print("Null")

def deleteNode(head, nodetoDelete):
	if head == nodetoDelete:
		return head.next

	currentNode = head
	while currentNode.next and currentNode.next != nodetoDelete:
		currentNode = currentNode.next

	if currentNode.next is None:
		return head

	currentNode.next = currentNode.next.next
	return head

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

printNode(node1)

delete = deleteNode(node1, node4)

printNode(delete)
