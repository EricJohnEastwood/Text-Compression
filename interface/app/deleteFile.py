import getpass
import os

def DeleteFile(Dictionary,base_dir):


	delFilename = input("Enter the filename :")
	delPassword = getpass.getpass("Enter the password :")
	if delFilename in Dictionary.keys():
		if Dictionary[delFilename][0] == delPassword:
			delBinary = Dictionary[delFilename][2]
			os.remove(os.path.join(base_dir,"binary",delBinary + ".data"))

			del Dictionary[delFilename]
			print("Done")
			return Dictionary

		else:
			print("Wrong password")

	else:
		print("Wrong Filename or Password")



