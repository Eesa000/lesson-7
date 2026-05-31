# python code to demonstrate how parent constructors
# are called.

# parent class
class person( object ):

        # __init__ is known as the constructor
        def __init__(self, name, idnumber):
            self.name = name
            self.idnumber = idnumber
        def display(self):
            print(self.name)
            print(slef.idnumber)

# child class
class employee( person ):
    def __init__(self, name, idnumber, salary, post):
            self.salary = salary
            self.post = post

            # invoking the __init__ of the parent class
            person.__init__(self, name, idnumber)


# creation of an object variable or an instance
a = employee('rahul', 886012, 200000, "intern")

# calling a function of the class person using its instance
a.display()