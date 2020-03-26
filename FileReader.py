import csv

class FileReader:
	def __init__(self):
		self.file = None
		self.reader = None
		self.currentLine = 1

	def openFile(self, fileName):
		self.file = open(fileName, newline='')
		self.reader = csv.reader(self.file, quoting=csv.QUOTE_NONE)
#		for row in self.reader:
#			print(row)

	def getNumRecords(self):
		return len(self.lines) - 1

	def nextLine(self):
		line = self.lines[self.currentLine]
		self.currentLine += 1
		return line
