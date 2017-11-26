from os import path
import sys

# read the text an give the list of frequency as well as location
def readText(filename,base_dir):
	location = path.join(base_dir,"text",filename)
	words = open(location)

	usingWords = words.read()
	words.close()

	# print(sys.getsizeof(usingWords))
	providingDict = getTimes(usingWords)
	
	list1 = []
	for x in providingDict.keys():
		list1.append([x,providingDict[x]])

	for i in list1:
		i[1] = int(i[1])

	return list1,location


# get the frequency
def getTimes(usingWords):
	dictionary = {}

	for i in range(len(usingWords)):
		if(usingWords[i] not in dictionary.keys()):
			dictionary.update({usingWords[i]:1})
		else:
			for x in dictionary.keys():
				if(usingWords[i] == x):
					dictionary[x] += 1

	return dictionary