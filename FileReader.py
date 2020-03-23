class FileReader:
	def __init__(self):
		self.file = None
		self.lines = None
		self.currentLine = 1

	def openFile(self, fileName):
		self.file = open(fileName, "r")
		self.lines = self.file.readlines()

	def getNumRecords(self):
		#count = 0
		#for l in self.file:
		#	count += 1
		#count -= 1 # substract one for header
		return len(self.lines) - 1

	def nextLine(self):
		line = self.lines[self.currentLine]
		self.currentLine += 1
		return line
