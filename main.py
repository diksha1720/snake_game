from snake import Snake
from turtle import Screen
import time
from food import Food
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

flag = True
while flag:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 25:
        scoreboard.increase_score()
        food.refresh()
        snake.extend()

    #Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor()<-280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        snake.restart()



    #Detect colission with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            snake.restart()





screen.exitonclick()








