from Calculator import Calculator
from FileReader import FileReader

def test_calc_sqr():
	calc = Calculator()
	fr = FileReader()
	fr.openFile('csvFiles/UnitTestSquare.csv')

	for row in fr.reader:
		if calc.sqr(int(row['Value 1'])) == round(float(row['Result']),3):
			continue
		else:
			assert False

	assert True


