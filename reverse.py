class Reverse:
    def __init__(self, s=""):
        self.s = s

    def reverse_string(self):
        words = self.s.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)


# User input
s = input("Enter a string: ")

# Create object
obj = Reverse(s)

# Display reversed string
print("Reversed string:", obj.reverse_string())