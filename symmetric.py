# Program to find the symmetric difference between two sets

# Example A
set1 = {'blue', 'green'}
set2 = {'blue', 'yellow'}

result_a = set1.symmetric_difference(set2)

print("Example A")
print("Set1:", set1)
print("Set2:", set2)
print("Symmetric Difference:", result_a)
print()

# Example B
set3 = {1, 2, 3, 4, 5}
set4 = {1, 5, 6, 7, 8, 9}

result_b = set3.symmetric_difference(set4)

print("Example B")
print("Set1:", set3)
print("Set2:", set4)
print("Symmetric Difference:", result_b)