from StatsCalc import StatsCalc
from FileReader import FileReader

def test_stats_calc():
	fr = FileReader()
	fr.openFile('csvFiles/testFile.csv')
	statsCalc = statsCalc()

	if statsCalc.populationMean() != 5120.729:
		assert False
	if stastCalc.populationMode() != 3488:
		assert False

	assert True


