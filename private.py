# class creation
class myclass:

    # private variable
    __privatevar = 27

    # private method
    def __privMeth(self):
        print("i'm inside class my class")

    # function to print value of private variable
    def hello(self):
        print("private variable value: ",self.__privatevar)

# object creation and method call
foo = myclass()
foo.hello()
foo.__privMeth