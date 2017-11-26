from function.convert_text import convertText
from os import path
import getpass

def Getfile(Dictionary,base_dir):
	# get filename and password
	Filename = input("Enter filename : ")
	Password = getpass.getpass("Enter password : ")

# check in dictionary and then get the location and decode and write it into the file in text folder
	if(Filename in Dictionary.keys()):
		if Dictionary[Filename][0] == Password:
			filename = Dictionary[Filename][2]
			decoded = convertText(filename,base_dir)
			# print(decoded)
			words = open(path.join(base_dir,"text",Filename),"w+")
			words.write(decoded)
			words.close()
			print("Done")


		else:
			print("Wrong Password")
			return




	else:
		print("Invalid Filename")
		return