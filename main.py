import random
import turtle as t

# Turtle features
tim = t.Turtle()
tim.hideturtle()
tim.speed(4)
tim.pen(pensize=8)

# Turtle starting position
tim.penup()
tim.setx(0)
tim.sety(100)
tim.pendown()

# Color properties
t.colormode(255)


# Turtle generates a random walk with random colors
# Function for moving
def turn_and_move():
    directions = [0, 90, 180, 270]
    direction = random.randint(0, 3)

    tim.setheading(directions[direction])
    tim.forward(20)


# Change Turtle color
def change_color():
    # Create a random color using a tuple
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    color = (r, b, g)
    return color




# Turtle drawing a a square using angle
for x in range(100):
    tim.color(change_color())
    turn_and_move()


screen = t.Screen()
screen.exitonclick()
