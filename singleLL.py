#!/usr/bin/python3

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

def traverse(head):
	currentNode = head
	while currentNode:
		print(currentNode.data, end="->")
		currentNode = currentNode.next
	print("Null")

node1 = Node(5)
node2 = Node(12)
node3 = Node(7)
node4 = Node(32)

node1.next = node2
node2.next = node3
node3.next = node4

traverse(node1)
