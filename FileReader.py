class FileReader:
	def openFile(fileName):
		file = open(fileName, "r")
		print(file.read())
