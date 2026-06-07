class myclass:
	__privatevar = 27

	def __privMeth(self):
		print("i'm inside class my class")

	def hello(self):
		print("private variable value:", self.__privatevar)
		self.__privMeth()  # Calling the private method internally works perfectly


if __name__ == '__main__':
	foo = myclass()
	foo.hello()

	# Accessing the name-mangled private method from outside (not recommended):
	foo._myclass__privMeth()  # Notice the single underscore + class name prefix