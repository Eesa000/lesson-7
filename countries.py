# class 1
class india():
    def capital(self):
        print("New Delhi is the capital of india.")

    def language(self):
        print("Hindi is the most widely spoken language of india.")

    def type(self):
        print("India is a developing country.")

# class 2
class usa():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("english is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")

# object creation
obj_ind = india()
obj_usa = usa()

# common interface
for country in [obj_ind, obj_usa]:
    country.capital()
    country.language()
    country.type()