from StatsCalc import StatsCalc
from FileReader import FileReader

def test_stats_calc():
	fr = FileReader()
	statsCalc = StatsCalc()

	if statsCalc.populationMean() != 5120.729:
		assert False
	if statsCalc.populationMode() != 3488:
		assert False
	if statsCalc.median() != 5183:
		assert False
	if statsCalc.standardDev() != 2897.721:
		assert False
	if statsCalc.variance != 8396786.683:
		assert False
	assert True


