import math

# ask user for angle in degrees
angle_deg = float(input("Enter angle in degrees: "))

# convert degrees to radians because math.sin, cos, tan use radians
angle_rad = math.radians(angle_deg)

# calculate trigonometric values
sine_value = math.sin(angle_rad)
cosine_value = math.cos(angle_rad)
tangent_value = math.tan(angle_rad)

# display results
print("sin(", angle_deg, ") =", sine_value)
print("cos(", angle_deg, ") =", cosine_value)
print("tan(", angle_deg, ") =", tangent_value)
