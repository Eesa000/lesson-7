# import necessary packages
from abc import ABC, abstractmethod
# create a base class
class animal(ABC):

    # abstract method
    # should be implemented by all sub-classes
    # def move(self):
          pass

# sub classes
class human(animal):
        
    def move(self):
        print("I can walk and run")

class snake(animal):
      
    def move(self):
        print("I can crawl")

class dog(animal):
     
    def move(self):
          print("I can bark")

class lion(animal):
           
    def move(self):
          print("I can roar")

# driver code
R = human()
R.move()

K = snake()
K.move()

R = dog()
R.move()

K = lion()
K.move()