from Calculator import Calculator
from FileReader import FileReader

def test_calc_add():
	calc = Calculator()
	fr = FileReader()
	fr.openFile('csvFiles/UnitTestAddition.csv')

	for row in fr.reader:
		if calc.add(int(row['Value 1']), int(row['Value 2'])) == int(row['Result']):
			continue
		else:
			assert False

	assert True


