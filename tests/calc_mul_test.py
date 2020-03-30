from Calculator import Calculator
from FileReader import FileReader

def test_calc_mul():
	calc = Calculator()
	fr = FileReader()
	fr.openFile('csvFiles/UnitTestMultiplication.csv')

	for row in fr.reader:
		if calc.mul(int(row['Value 1']), int(row['Value 2'])) == int(row['Result']):
			continue
		else:
			assert False

	assert True


