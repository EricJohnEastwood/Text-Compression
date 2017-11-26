from interface.app.getfile import Getfile
from interface.app.createfile import Createfile
import os
import json


# cycle between the various options
def Mainmenu(Dictionary,base_dir):
	while True:
		# open the dictionary containing the info and load the data
		if os.stat(os.path.join(base_dir,"data.json")).st_size != 0:
			with open(os.path.join(base_dir,"data.json"),"r") as dta:
				Dictionary = json.load(dta)

		print("MAIN MENU \n 1.Get the Text \n 2.Make a text \n 3.Quit")

		choice = input("enter you choice (1/2/3):")

		if choice == '1':
			Getfile(Dictionary,base_dir)

		elif choice == '2':
			Createfile(Dictionary,base_dir)
			# update the data
			with open(os.path.join(base_dir,"data.json"),"w+") as data:
				json.dump(Dictionary,data)

		elif choice == '3':
			return Dictionary

		else:
			print("Wrong Choice")
			return Dictionary