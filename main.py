from turtle import Turtle, Screen
import random
tim = Turtle()

tim.shape("turtle")
tim.color("red")
colours = ["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen"]
x = 3
tim.pensize(5)

while (x<=10):
    j = 0
    #tim.color(random.choice(colours))
    while j<x:

        tim.forward(100)
        tim.right(360//x)
        j+=1
    x+=1


screen = Screen()
screen.exitonclick()
