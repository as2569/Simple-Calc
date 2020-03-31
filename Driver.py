from FileReader import FileReader
from StatsCalc import StatsCalc
from Calculator import Calculator

#calc = Calculator()
statsCalc = StatsCalc()
#statsCalc.fr.fixFile()

#fr = FileReader()
#fr.openFile('tests/csvFiles/testCSV.csv')

print(str(statsCalc.populationMean()))
print(str(statsCalc.populationMode()))


