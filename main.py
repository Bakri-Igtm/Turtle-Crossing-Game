import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.bgcolor("grey")
screen.tracer(0)

scoreboard = Scoreboard()
car_manager = CarManager()

my_player = Player()
screen.listen()
screen.onkey(my_player.go_up, "Up")
screen.onkey(my_player.go_down, "Down")
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #Detect car collision
    for car in car_manager.all_cars:
        if car.distance(my_player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Detect successful crossing
    if my_player.at_finishline():
        my_player.to_start()
        car_manager.level_up()
        scoreboard.increase_level()








screen.exitonclick()