from StatsCalc import StatsCalc
from FileReader import FileReader

def test_stats_calc():
	fr = FileReader()
	statsCalc = StatsCalc()

	if statsCalc.populationMean() != 5120.729:
		assert False
	if statsCalc.populationMode() != 3488:
		assert False

	assert True


