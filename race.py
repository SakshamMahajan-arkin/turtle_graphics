from turtle import Turtle,Screen
import random

is_race_on = False
screen=Screen()
screen.setup(width=500,height=400)
colors=["red","orange","yellow","green","blue","purple"]

user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race")
li=30;
all=[]


for turtle_index in range(0,6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-238, y=-100+li)
    li+=30
    all.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:

    for t in all:
        if (t.xcor()>230):
            win=t.pencolor()
            if (win==user_bet):
                print("CONGO")
            else:
                print("LOST")
            is_race_on=False
            continue
        rand_dis=random.randint(0,10);
        t.forward(rand_dis)

screen.exitonclick()