import random
from turtle import *
from Snake_File import *


class Food():
    def __init__(self):
        # Create a turtle to represent the food
        self.tim = Turtle()
        self.tim.penup()         # Don't draw lines when moving the food
        self.tim.hideturtle()    # Hide the turtle icon, just show the dot
        print(self.tim.pos())    # Debug: print initial position
        self.refresh()           # Place the food at a random location

    def refresh(self):
        # Remove the old food dot (if any)
        self.tim.clear()
        # DSA: Randomization - choose a new random position for the food
        rand_x = random.randint(-200, 200)
        rand_y = random.randint(-200, 200)
        # Move the food to the new random position
        self.tim.goto(rand_x, rand_y)
        # Draw the food as a colored dot
        self.tim.dot(20, 'cyan')