import pickle
import sys
from os import path

# opening and dumbing 
def convertBinary(Tree,location,base_dir):
	encoded = convertToBinary(Tree,location)
	# print(encoded)
	# print(sys.getsizeof(encoded))

	x = input(" Enter BinaryFileName to save to:")

	f = open(path.join(base_dir,"binary",x + ".data"),"wb+")

	pickle.dump([encoded,Tree],f)
	f.close()
	
	return x

factor_size = 15000
max_string = '11111111'

# Called by convertBinary to make the binary lists(as they will be in pieces) and then
# these list of lists are sent back .
def convertToBinary(tree,location):
	# print(location)
	words = open(location)
	usingWords = words.read()
	list = []
	bin = ''
	# print(sys.getsizeof(usingWords))
	length = sys.getsizeof(usingWords)//factor_size
	# print(length)
	

	# for loop cut the whole data and takes pieces of getsize "around factor size"
	# this loop for all full size pieces
	for i in range(len(usingWords)):
		bin = find(usingWords[i],tree,bin)
		if(sys.getsizeof(bin) >= factor_size  and sys.getsizeof(bin) < factor_size + sys.getsizeof(max_string) and length != 0):
			length -= 1
			if(bin[0] == '0'):
				bin = '1' + bin
				# print(bin)
				list.append([False,(int(bin,2))])

			else:
				# print(bin)
				list.append([True,(int(bin,2))])
			# print(bin)
			bin = ''
		if(length == 0):
			# print(i)
			usingWords = usingWords[i:]
			break

	bin = ''

	#this loops takes into account the last part which is smaller than factor size
	for i in range(len(usingWords)):
		bin = find(usingWords[i],tree,bin)

	if(bin[0] == '0'):
		bin = '1' + bin
		#print(bin)
		list.append([False,(int(bin,2))])

	else:
		#print(bin)
		list.append([True,(int(bin,2))])
		#print(bin)

	# print(list)
	return list

# does the sole purpose of running through Tree with each character and find its location 
# via Hufmann algorithm
def find(value,tree,bin):

	if(tree[0][0] == value):
		return bin
	
	else:
		[v,_,subtree] = tree[0]
		st =subtree
		# if found in left hand put 0 else put 1
		if value in st[0][0]:
			bin += '0'
			return find(value,[st[0]],bin)

		else:
			bin += '1'
			return find(value,[st[1]],bin)

	return bin
