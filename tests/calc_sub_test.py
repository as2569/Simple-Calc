from Calculator import Calculator
from FileReader import FileReader

def test_calc_sub():
	calc = Calculator()
	fr = FileReader()
	fr.openFile('csvFiles/UnitTestSubtraction.csv')

	for row in fr.reader:
		if calc.sub(int(row['Value 2']), int(row['Value 1'])) == int(row['Result']):
			continue
		else:
			assert False

	assert True


