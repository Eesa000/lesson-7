a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))
c = int(input("Enter the third number (c): "))

print("\nBefore swapping:")
print("a =", a)
print("b =", b)
print("c =", c)

# Swapping the values (e.g., rotate right: a -> b, b -> c, c -> a)
temp = a
a = b
b = c
c = temp

print("\nAfter swapping:")
print("a =", a)
print("b =", b)
print("c =", c)