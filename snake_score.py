from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        #self.write(f"Score: {self.score}",align="center",font=("Arial",24,"normal"))
        self.update()
        self.hideturtle()

    def update(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score+=1
        #self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.clear()
        self.update()

    def gameover(self):
        self.goto(0,0)
        self.write("Game over", align="center", font=("Arial", 24, "normal"))