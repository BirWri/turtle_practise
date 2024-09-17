import random
from turtle import Turtle, Screen

# Turtle features
tim = Turtle()
#tim.hideturtle()
tim.shape("turtle")
tim.color("red")

# Turtle starting position
#tim.penup()
#tim.setx(-300)
#tim.sety(0)
#tim.showturtle()

# Turtle drawing a dashed line
#while tim.xcor() < 300:
#    print(tim.xcor())
#    tim.pendown()
#    tim.forward(10)
#    tim.penup()
#    tim.forward(10)

#TODO:1 rename the inputs to the functions. having same name isnt the best
#TODO:2 Can you find a better way to randomise the color of the turtle than a list

# Turtle drawing different shapes
# Create a function that devides 360 with an integer and returns the result
def calculate_angle(current_nr_of_angle):
    return 360/current_nr_of_angle


# Change Turtle color
def change_color():
    turtle_colors=["red", "blue", "green", "yellow", "brown", "pink"]
    tim.color(turtle_colors[random.randint(0, 5)])


# Draw the shape
def draw_shape(angle, current_nr_of_angle):
    for x in range(current_nr_of_angles):
        tim.forward(100)
        tim.rt(angle)


# Have a counter which start from 4 and goes up each iteration
current_nr_of_angles = 4
max_nr_of_angles = 10
# Have a for loop or a while look to draw all og the shapes

# Turtle drawing a a square using angle
while max_nr_of_angles - current_nr_of_angles != 0:
    angle = calculate_angle(current_nr_of_angles)
    change_color()
    draw_shape(angle, current_nr_of_angles)
    current_nr_of_angles += 1





screen = Screen()
screen.exitonclick()
