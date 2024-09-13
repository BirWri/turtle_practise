from turtle import Turtle, Screen

# Turtle features
tim = Turtle()
tim.hideturtle()
tim.shape("turtle")
tim.color("red")

# Turtle starting position
tim.penup()
tim.setx(-300)
tim.sety(0)
tim.showturtle()

# Turtle drawing a dashed line
while tim.xcor() < 300:
    print(tim.xcor())
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)

screen = Screen()
screen.exitonclick()
