from Calculator import Calculator
from FileReader import FileReader

def test_calc_sqrRoot():
	calc = Calculator()
	fr = FileReader()
	fr.openFile('csvFiles/UnitTestSquareRoot.csv')

	for row in fr.reader:
		if calc.sqrRoot(int(row['Value 1'])) == round(float(row['Result']),3):
			continue
		else:
			assert False

	assert True


