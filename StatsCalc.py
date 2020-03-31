from FileReader import FileReader
from Calculator import Calculator
import csv

class StatsCalc:
	def __init__(self):
		self.fr = FileReader()
		self.calc = Calculator()
		self.setup()

	def setup(self):
		self.fr.openFile('tests/csvFiles/testFile.csv')
		print("num records " + str(self.fr.numRecords))
		self.fr.closeFile()

	def populationMean(self):
		sum = 0
		numRows = 0
		with open('tests/csvFiles/testFile.csv') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',', quoting=csv.QUOTE_NONE)
			for row in csv_reader:
				sum += float(row[0])
				numRows += 1
		return self.calc.div(sum, numRows)

	def populationMode(self):
		modeDict = {}
		with open('tests/csvFiles/testFile.csv') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',', quoting=csv.QUOTE_NONE)
			for row in csv_reader:
				val = int(row[0])
				if val in modeDict:
					modeDict[val] = modeDict[val] + 1
				else:
					modeDict[val] = 1

			topValue = 0
			topKey = None
			for key in modeDict:
				if modeDict[key] > topValue:
					topValue = modeDict[key]
					topKey = key

		return topKey

