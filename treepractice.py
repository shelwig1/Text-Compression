
class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

	def insert(self, data):
		if self.data:
			if data < self.data:
				if self.left == None:
					self.left = Node(data)
				else:
					self.left.insert(data)
			elif data > self.data:
				if self.right is None:
					self.right = Node(data)
				else:
					self.right.insert(data)
		else:
			self.data = data

	def printTree(self):
		if self.left:
			self.left.printTree()
		print(self.data)
		if self.right:
			self.right.printTree()


			#keep going until there is no self.left
#building and traversing a tree

#inorder - left root rigth
def printinorder(root):
	#all the way down to the left most root
	if root.left:
		printinorder(root.left)
	print(root.data)
	if root.right:
		printinorder(root.right)

#preorder - root left right
def preorder(root):
	print(root.data)
	if root.left:
		preorder(root.left)
	if root.right:
		preorder(root.right)

#postorder - left right root
def postorder(root):
	if root.left:
		postorder(root.left)
	if root.right:
		postorder(root.right)
	print(root.data)
			
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

#breadth first traversal / level order traversal



#printinorder(root)
#preorder(root)
#postorder(root)