from FileReader import FileReader
from StatsCalc import StatsCalc
from Calculator import Calculator


calc = Calculator()
fr = FileReader()
fr.openFile('csvFiles/testCSV.csv')

for row in fr.reader:

