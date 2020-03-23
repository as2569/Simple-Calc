class FileReader:
	def openFile(self, fileName):
		file = open(fileName, "r")
		line = file.next() # to ignore header

	def getNumRecords(self):
		count = 0
		for line in f:
			count += 1
		count -= 1 # substract one for header
		return count

	def nextLine(self):
		line = file.next()
		return line
