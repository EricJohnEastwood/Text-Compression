import getpass
from function.dict import readText
from function.make_tree import makeTree
from function.convert_binary import convertBinary
import sys

# most names are self explanatory
# the convertBinary means function to convert the Tree into encoded form
def Createfile(Dictionary,cw):

# create the file in encoded form and save it in binary folder
	tempFilename = input("Enter Filename : ")
	tempPassword = getpass.getpass("Enter password : ")
	if(tempFilename not in Dictionary.keys()):

		listOfFrequency,location = readText(tempFilename,cw)
		Tree = makeTree(listOfFrequency)
		# print(sys.getsizeof(Tree))
		filename = convertBinary(Tree,location,cw)

		tempLocation = location
		tempBinary = filename
	

		Dictionary.update({tempFilename:[tempPassword,tempLocation,tempBinary]})

	else:
		print("Name already exist : ")
		print("Want to over write? : ")
		n = input("Yes/No : ")


		if(n == 'Yes' or n == 'yes' or n == 'YES'):
			listOfFrequency,location = readText(tempFilename,cw)
			Tree = makeTree(listOfFrequency)
			print(sys.getsizeof(Tree))
			filename = convertBinary(Tree,location,cw)

			tempLocation = location
			tempBinary = filename

			Dictionary[tempFilename] = [tempPassword,tempLocation,tempBinary]

		else:
			sys.exit()

	return Dictionary
