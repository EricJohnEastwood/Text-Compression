
from config import Dictionary
from interface.app.mainmenu import Mainmenu
import os

base_dir = os.getcwd()

# calls mainmenu
Dictionary = Mainmenu(Dictionary,base_dir)

exit()
