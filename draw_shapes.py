from turtle import Screen, Turtle
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def move():
    for i in range(3, 10):
        timmy.color(random.choice(colours))
        for n in range(i):
            timmy.forward(100)
            timmy.right(360 / i)


timmy = Turtle()
timmy.shape("turtle")
timmy.color("green") 
move()

screen = Screen()
screen.exitonclick()