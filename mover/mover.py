from shutil import move, copy2
from os import path, mkdir
from datetime import datetime
from re import compile, findall
from glob import glob

class Transfer(object):

	def __init__(self, method, destination, source = "G:/"): 
		self.method = method
		self.destination = destination
		self.source = source

	def do(self):
		photo_num = 0
		file_paths = glob((str(self.source)+ "*/*/*.RW2")) 

		if not file_paths:
			raise Exception("Invalid Source or no RW2 files to be found")

		if not path.exists(self.destination):
			mkdir(self.destination)

		regex = compile(("P\d.*\..*"))

		for a_file in file_paths:
			file_name = regex.findall(a_file).pop()
			
			if self.method == "move":	
				move(a_file, self.destination)
				print "%s successfully moved" % (file_name)

			elif self.method == "copy":
				copy2(a_file, self.destination)
				print "%s successfully copied" % (file_name)

			photo_num += 1

		if self.method == "move":
			print "%i files successfully moved." % (photo_num)
			
		elif self.method == "copy":
			print "%i files successfully copied." % (photo_num)
			

if __name__ == '__main__':
	folder_name = raw_input("What would you like to call the folder? \n> ")

	if folder_name == "":
		current_date = datetime.now()
		folder_name = current_date.strftime("%Y-%m-%d")

	backup_drive = "E:/Photos/%s/" % (folder_name)

	choice = raw_input("\nmove or copy?\n> ").lower()

	while True:

		if choice in ["move", "m"]:
			move_files = Transfer("move", backup_drive)
			move_files.do()
			break

		elif choice in ["copy", "c"]:
			copy_files = Transfer("copy", backup_drive) 
			copy_files.do()
			break

		else:
			choice = raw_input('Please enter either "move" or "copy"\n> ').lower()

	raw_input()
