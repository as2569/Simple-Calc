from FileReader import FileReader
from Calculator import Calculator
import csv

class StatsCalc:
	def __init__(self):
		self.fr = FileReader()
		self.calc = Calculator()
		self.data = []
		self.setup()

	def setup(self):
		with open('tests/csvFiles/testFile.csv') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',', quoting=csv.QUOTE_NONE)
			for row in csv_reader:
				self.data.append(int(row[0]))

	def populationMean(self):
		sum = 0
		for i in range(len(self.data)):
			sum += self.data[i]
		return self.calc.div(sum, len(self.data))

	def populationMode(self):
		modeDict = {}
		for i in range(len(self.data)):
			val = self.data[i]
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

	def standardDev(self):
		mean = self.populationMean()
		sqrDiff = 0
		for i in range(len(self.data)):
			val = self.calc.sub(self.data[i], int(mean))
			val = self.calc.sqr(val)
			sqrDiff += val
		foo = self.calc.div(sqrDiff, len(self.data))
		return self.calc.sqrRoot(foo)
