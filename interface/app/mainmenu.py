from interface.app.getfile import Getfile
from interface.app.createfile import Createfile
from interface.app.deleteFile import DeleteFile
import os
import json


# cycle between the various options
def Mainmenu(Dictionary,base_dir):
	while True:
		# open the dictionary containing the info and load the data
		if os.stat(os.path.join(base_dir,"data.json")).st_size != 0:
			with open(os.path.join(base_dir,"data.json"),"r") as dta:
				Dictionary = json.load(dta)

		print("MAIN MENU \n 1.Get Text \n 2.Create text \n 3.Delete text \n 4.Quit")

		choice = input("enter you choice (1/2/3):")

		if choice == '1':
			Getfile(Dictionary,base_dir)

		elif choice == '2':
			Createfile(Dictionary,base_dir)
			# update the data
			with open(os.path.join(base_dir,"data.json"),"w+") as data:
				json.dump(Dictionary,data)

		elif choice == '3':
			
			Dictionary = DeleteFile(Dictionary,base_dir)
			
			with open(os.path.join(base_dir,"data.json"),"w+") as data:
				json.dump(Dictionary,data)


		elif choice == '4':
			return Dictionary

		else:
			print("Wrong Choice")
			return Dictionary