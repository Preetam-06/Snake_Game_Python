from turtle import *

move_dist = 20  # How far the snake moves each step

#----------CLASS-----------------
class SnakeSegment():
    #-----------CONSTRUCTOR---------------------------
    def __init__(self):
        self.segments = []  # DSA: List to store all snake segments (dynamic array)

    #----------CREATE_SNAKE ----------------------------
    def create_snake(self, n):
        self.n = n
        for pos in range(self.n):
            snake_segment = Turtle('circle')  # Each segment is a turtle object (node in the list)
            if pos == 0:
                snake_segment.color("grey")   # Head segment is grey (distinguish visually)
            else:
                snake_segment.shape("circle")
                snake_segment.color("white")  # Body segments are white
            snake_segment.penup()             # Don't draw lines between segments
            snake_segment.goto(snake_segment.pos())  # Place at default position (0,0)
            snake_segment.speed(0)
            self.segments.append(snake_segment)  # DSA: Add segment to the list

    #----------ADD_SEGMENT (used for growing the snake)----------------------------
    def add_snake(self, n):
        snake_segment = Turtle("circle")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(n)  # DSA: Place new segment at the given position (usually the tail)
        snake_segment.speed(0)
        self.segments.append(snake_segment)  # DSA: Append to the list

    #----------EXTEND (called when snake eats food)--------------------------------
    def extend(self):
        # DSA: Add a new segment at the position of the last segment (tail)
        self.add_snake(self.segments[-1].position())

    #------------MOVE_FUNCTION (core snake movement logic)--------------------------
    def move(self):
        # DSA: Shift each segment to the position of the one in front (like shifting array elements)
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(move_dist)  # Move the head forward

    #-----------TURN_LEFT (event handler)---------------------------
    def left1(self):
        if self.segments[0].heading() != 0:  # Prevent reversing direction
            self.segments[0].setheading(180)

    #-----------TURN_RIGHT (event handler)--------------------------
    def right1(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    #-----------TURN_UP (event handler)-----------------------------
    def up1(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    #-----------TURN_DOWN (event handler)---------------------------
    def down1(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)