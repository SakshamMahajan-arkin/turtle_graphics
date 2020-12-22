from turtle import Turtle
start=[(0,0),(-20,0),(-40,0)]

class Snake:
    def __init__(self):
        self.segment=[]
        self.create_snake()
        self.up()
        self.down()
        self.right()
        self.left()

    def create_snake(self):
        for position in start:
            new = Turtle("square")
            new.color("white")
            new.penup()
            new.goto(position)
            self.segment.append(new)

    def extend(self):
        new = Turtle("square")
        new.color("white")
        new.penup()
        new.goto(self.segment[-1].position())
        self.segment.append(new)

    def move(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            self.segment[seg].goto(self.segment[seg - 1].xcor(), self.segment[seg - 1].ycor())
        self.segment[0].forward(20)

    def up(self):
        if self.segment[0].heading() !=270:
            self.segment[0].setheading(90)

    def down(self):
        if self.segment[0].heading() != 90:
            self.segment[0].setheading(270)

    def left(self):
        if self.segment[0].heading() != 0:
            self.segment[0].setheading(180)

    def right(self):
        if self.segment[0].heading() != 180:
         self.segment[0].setheading(0)