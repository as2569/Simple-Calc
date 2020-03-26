from Calculator import Calculator
from FileReader import FileReader

def test_calc_sqrRoot():
	calc = Calculator()
	fr = FileReader()
	fr.openFile('csvFiles/UnitTestSquareRoot.csv')

	for row in fr.reader:
		if calc.sqr(int(row[0])) == float(row[1]):
			continue
		else:
			assert False

	assert True


