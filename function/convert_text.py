from os import path
import pickle

# convert the elements of binary data file back to characters
def convertText(filename,base_dir):
	words = open(path.join(base_dir,"binary",filename + ".data"),"rb")
	fun = pickle.load(words)
	words.close()
	final = ''

	Tree = fun[1]


	for i in range(len(fun[0])):
		case,encoded = fun[0][i] 

		if(case == True):
			binary = bin(int(encoded))
			binary = binary[2:]

		else:
			binary = bin(int(encoded))
			binary = binary[3:]

		text = ""
		tree = Tree
		while(len(binary) > 0):

			text,binary = findFirst(binary,tree,text,Tree)

		final += text

	return final


# No particular use(extra code) but helpful as the brackets of the tree seemed to be having non uniformity
def findFirst(binary,tree,text,Tree):
	[v,_,subtree] = tree[0]
	st =subtree

	if(binary[0] == '0'):

		binary = binary[1:]
		return find(binary,st[0],text,Tree)

	else:
		binary = binary[1:]
		return find(binary,st[1],text,Tree)


# use the binary digits as an instruction to move through the tree 
def find(binary,tree,text,Tree):

	if(len(tree[0]) == 1 ):
		text += tree[0]
		return text,binary

	else:
		[v,_,subtree] = tree
		st =subtree

		if(binary[0] == '0'):
			binary = binary[1:]
			return find(binary,st[0],text,Tree)

		else:
			binary = binary[1:]
			return find(binary,st[1],text,Tree)
