from Calculator import Calculator
from FileReader import FileReader


def test_calc_div():
	calc = Calculator()
	fr = FileReader()
	fr.openFile('csvFiles/UnitTestDivision.csv')

	for row in fr.reader:
		if calc.div(int(row['Value 2']), int(row['Value 1'])) == round(float(row['Result']),3):
			continue
		else:
			assert False

	assert True


