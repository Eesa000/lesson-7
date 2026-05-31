class Dog:
    # Class variable
    animal = "Dog"

    # Constructor
    def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour

    # Method to display details
    def display_details(self):
        print("Animal :", Dog.animal)
        print("Breed  :", self.breed)
        print("Colour :", self.colour)
        print()


# Creating objects
dog1 = Dog("German Shepherd", "Black and Tan")
dog2 = Dog("Labrador", "Golden")

# Displaying details
print("Details of Dog 1")
dog1.display_details()

print("Details of Dog 2")
dog2.display_details()