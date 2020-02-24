class Calculator:
	def add(self, num1, num2):
		return num1 + num2

	def sub(self, num1, num2):
		return num1 - num2

	def mul(self, num1, num2):
		return num1 * num2

	def div(self, num1, num2):
		return num1 / num2

if __name__ == "__main__":
	c = Calculator()
	print(c.add(1,2))
	print(c.sub(4,3))
	print(c.mul(4,3))
	print(c.div(0,4))
