import random
from turtle import Turtle, Screen

# Turtle features
tim = Turtle()
tim.hideturtle()
tim.speed(4)
tim.pen(pensize=8)

# Turtle starting position
tim.penup()
tim.setx(0)
tim.sety(100)
tim.pendown()


# Turtle generates a random walk with random colors
# Function for moving
def turn_and_move():
    directions = [0, 90, 180, 270]
    direction = random.randint(0, 3)

    tim.setheading(directions[direction])
    tim.forward(20)


# Change Turtle color
def change_color():
    turtle_colors=["red", "blue", "green", "yellow", "brown", "pink", "light gray"]
    tim.color(turtle_colors[random.randint(0, len(turtle_colors)-1)])


# Turtle drawing a a square using angle
for x in range(100):
    change_color()
    turn_and_move()


screen = Screen()
screen.exitonclick()
