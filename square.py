import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")  # background color
screen.title("Drawing a Square with Turtle")

# Create the turtle
pen = turtle.Turtle()
pen.color("green")   # turtle line color
pen.pensize(3)       # thickness of the lines
pen.speed(3)         # drawing speed

# Draw a square
for _ in range(4):
    pen.forward(100)  # move forward 100 units
    pen.right(90)     # turn right by 90 degrees

# Finish
turtle.done()
