from turtle import  Screen
import time
from snake import Snake
from snake_food import Food
from snake_score import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food=Food()
score=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if (snake.segment[0].distance(food))<15:
        food.refresh()
        # screen.update()
        snake.extend()
        score.increase_score()

    if snake.segment[0].xcor() > 280 or snake.segment[0].xcor() < -280 or snake.segment[0].ycor() > 280 or snake.segment[0].ycor() < -280:
        game_is_on=False
        score.gameover()

    for seg in snake.segment:
        if (seg==snake.segment[0]):
            continue
        if snake.segment[0].distance(seg)<10:
            game_is_on = False
            score.gameover()

screen.exitonclick()