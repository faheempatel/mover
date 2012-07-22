import shutil
import os
import datetime
import re

class Transfer(object):
	def __init__(self, method, destination, source = "G:/"): 
		self.method = method
		self.destination = destination
		self.source = source

	def do(self):
		photo_num = 0
		file_paths = []

		raw = (".3fr", ".ari", ".arw", ".srf", ".sr2", ".bay", ".crw", ".cr2", 
			".cap", ".iiq", ".eip", ".dcs", ".dcr", ".drf", ".k25", ".kdc", 
			".dng", ".erf", ".fff", ".mef", ".mos", ".mrw", ".nef", ".nrw", 
			".orf", ".pef", ".ptx", ".pxn", ".r3d", ".raf", ".raw", ".rw2", 
			".rwl", ".rwz", ".srw", ".x3f", ".obm")
		#jpeg = (".jpeg", ".jpg")

		for root, __, files in os.walk(self.source):
			for file in files:
				if file.lower().endswith(raw): #or name.lower().endswith(jpeg)):
					file_path = os.path.join(root, file)
					file_paths.append(file_path)

		if not file_paths:
			raise Exception("Invalid Source or no RAW files to be found")

		if not os.path.exists(self.destination):
			os.mkdir(self.destination)

		regex = re.compile(r"[\w-]+\.\w+")
		process = "moved" if self.method == "move" else "copied"

		for photo in file_paths:
			photo_name = regex.findall(photo).pop()
			
			if self.method == "move":	
				shutil.move(photo, self.destination)
			else:
				shutil.copy2(photo, self.destination)

			print "%s %s" % (photo_name, process)
			photo_num += 1

		plural = "files" if photo_num > 1 else "file"
		print "\n%i %s successfully %s." % (photo_num, plural, process)
			
if __name__ == '__main__':
	folder_name = raw_input("What would you like to call the folder? \n> ")

	# If no folder name is entered: current date will be the folder's name.
	if folder_name == "":
		current_date = datetime.datetime.now()
		folder_name = current_date.strftime("%Y-%m-%d")

	backup_drive = "E:/Photos/%s/" % (folder_name)

	choice = raw_input("\nmove or copy?\n> ")

	while True:
		if choice.lower() in ["move", "m"]:
			move_files = Transfer("move", backup_drive)
			move_files.do()
			break
		elif choice.lower() in ["copy", "c"]:
			copy_files = Transfer("copy", backup_drive) 
			copy_files.do()
			break
		else:
			choice = raw_input('Please type either "move" or "copy"\n> ')

	raw_input()
