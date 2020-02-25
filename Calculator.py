class Calculator:
	def add(self, num1, num2):
		return num1 + num2

	def sub(self, num1, num2):
		return num1 - num2

	def mul(self, num1, num2):
		return num1 * num2

	def div(self, num1, num2):
		return num1 / num2

	def sqr(self, num1):
		return num1 * num1

	def sqrRoot(self, num1):
		return num1 ** (1/2)

#if __name__ == "__main__":

c = Calculator()
cont = True

while cont == True:
	print('1 for add')
	print('2 for sub')
	print('3 for mul')
	print('4 for div')
	print('5 for square')
	print('6 for square root')
	print('q for quit')
	print('\n')

	choice = input('Enter choice ')
	if choice == 'q':
		cont = False
	elif choice == '1':
		n1 = input('Enter first number ')
		n2 = input('Enter second number ')
		print(n1 + ' + ' + n2 + ' = ' + str(c.add(float(n1), float(n2))))
	elif choice == '2':
		n1 = input('Enter first number ')
		n2 = input('Enter second number ')
		print(n1 + ' - ' + n2 + ' = ' + str(c.sub(float(n1), float(n2))))
	elif choice == '3':
		n1 = input('Enter first number ')
		n2 = input('Enter second number ')
		print(n1 + ' * ' + n2 + ' = ' + str(c.mul(float(n1), float(n2))))
	elif choice == '4':
		n1 = input('Enter first number ')
		n2 = input('Enter second number ')
		print(n1 + ' / ' + n2 + ' = ' + str(c.div(float(n1), float(n2))))
	elif choice == '5':
		n1 = input('Enter number ')
		print('Square of ' + n1 + ' = ' + str(c.sqr(float(n1))))
	elif choice == '6':
		n1 = input('Enter first number ')
		print('Square root of ' + n1 + ' = ' + str(c.sqrRoot(float(n1))))
	else:
		print('invalid input ')

	print('\n')
	#print(c.add(1,1))
	#print(c.sub(4,3))
	#print(c.mul(4,3))
	#print(c.div(0,4))
	#print(c.sqr(4))
	#print(c.sqrRoot(16))
