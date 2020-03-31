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

	def median(self):
		l = self.data
		l.sort()
		middle = int(len(l) / 2)
		return l[middle]

	def variance(self):
		mean = self.populationMean()
		values = 0;
		for i in range(len(self.data)):
			values += self.calc.sqr(self.calc.sub(self.data[i], mean))
		return self.calc.div(values, len(self.data))

	def zScore(self, index):
		z = self.calc.div(self.calc.sub(self.data[index], self.populationMean()), self.standardDev())
		return z

	def confidenceInterval(self):
		# z value for 95% confidence interval is 1.960
		top = self.populationMean() + 1.96 * (self.standardDev()/1000)
		bottom = self.populationMean() - 1.96 * (self.standardDev()/1000)
		return (top, bottom)

	def populationProportion(target, self):
		targetValue = 0
		for i in range(len(self.data)):
			if self.data[i] in target:
				targetValue += 0
		return targetValue / len(self.data)


