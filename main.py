from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) # Turns off animation on screen

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while True:
    screen.update() # Updates the screen
    time.sleep(0.12)
    game_is_on = snake.move()
    if not game_is_on:
        scoreboard.reset()
        snake.reset()
        game_is_on = True

    # Detect collision with food
    if snake.head.distance(food) < 17:
        food.refresh()
        snake.extends()
        scoreboard.increase_score()      
    


screen.exitonclick()