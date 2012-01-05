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

		# WIP - Don't like the nesting. FIX.
		for (root, dirs, files) in os.walk(self.source):
			for name in files:
				if name.lower().endswith(raw): #or name.lower().endswith(jpeg)):
					file_paths.append(os.path.join(root, name))

		if not file_paths:
			raise Exception("Invalid Source or no Raw files to be found")

		if not os.path.exists(self.destination):
			os.mkdir(self.destination)


		regex = re.compile("([-\w]+\.\w+)")

		for a_file in file_paths:
			file_name = regex.findall(a_file).pop()
			
			if self.method == "move":	
				shutil.move(a_file, self.destination)
				process = "moved"

			elif self.method == "copy":
				shutil.copy2(a_file, self.destination)
				process = "copied"

			print "%s successfully %s" % (file_name, process)

			photo_num += 1


		plural = "files" if photo_num > 1 else "file"
		
		print "\n%i %s %s." % (photo_num, plural, process)
			

if __name__ == '__main__':
	folder_name = raw_input("What would you like to call the folder? \n> ")

	if folder_name == "":
		current_date = datetime.datetime.now()
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
