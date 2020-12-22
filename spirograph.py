import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

directions = [0,90,180,270]
tim.speed("fastest")

def random_color():
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        randomc=(r,g,b)
        return randomc

def draw(size):
    for x in range(100):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading+10)
        tim.circle(100)

screen = t.Screen()
screen.exitonclick()
