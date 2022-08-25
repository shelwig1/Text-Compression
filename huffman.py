from sys import getsizeof

class node:
    def __init__(self, freq, symbol, left=None, right=None):
        # frequency of symbol
        self.freq = freq
 
        # symbol name (character)
        self.symbol = symbol
 
        # node left of current node
        self.left = left
 
        # node right of current node
        self.right = right
 
        # tree direction (0/1)
        self.huff = ''

#huffman coding
#frequency table

#build a tree out of the frequency table

def printNodes(node, val=''):
	newVal = val + str(node.huff)

	if(node.left):
		printNodes(node.left,newVal)
	if(node.right):
		printNodes(node.right,newVal)

	if(not node.left and not node.right):
		print(f"{node.symbol} -> {newVal}")



chars = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [ 5, 9, 12, 13, 16, 45]
nodes = []



#printNodes(nodes[0])

#decompression

#Create an encoded string
#abc
message = [
	[1100],
	[1101],
	[100]
]
def frequency(message):
	pass

def buildtree(chars,freq):
	nodes = []
	#frequency analysis
	for x in range(len(chars)):
	nodes.append(node(freq[x],chars[x]))

	while len(nodes) > 1:
		nodes = sorted(nodes, key=lambda x: x.freq)

		left = nodes[0]
		right = nodes[1]

		left.huff = 0
		right.huff = 1

		#left.symbol + right.symbol does what?
		newNode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)

		nodes.remove(left)
		nodes.remove(right)
		nodes.append(newNode)

	return nodes[0]

def encoding(message,root):
	#for each character in the message:
		#search through the tree for the character while building the huff code

def decoding(message, root):
	for i in message:
		pointer = nodes[0]
		for direction in str(i):
			if direction == '0':
				pointer = pointer.left
			if direction == '1':
				pointer = pointer.right

	return pointer.symbol