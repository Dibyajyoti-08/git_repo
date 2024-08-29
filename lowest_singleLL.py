#!/usr/bin/python3

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

def smallest(head):
	minValue = head.data
	currentNode = head.next
	while currentNode:
		if currentNode.data < minValue:
			minValue = currentNode.data
		currentNode = currentNode.next
	return minValue

node1 = Node(32)
node2 = Node(31)
node3 = Node(82)
node4 = Node(11)

node1.next = node2
node2.next = node3
node3.next = node4

print(smallest(node1))
