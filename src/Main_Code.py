from turtle import Turtle, Screen
import time
from Snake_File import SnakeSegment
from Snake_Food_File import Food
from Score_File import score_bd

# --- Create game objects ---
snake = SnakeSegment()        # Our snake, which is a list of Turtle segments
score1 = score_bd()           # Scoreboard (uses a Turtle for drawing text)
snake.create_snake(3)         # Start with 3 segments
food = Food()                 # Food object, randomly placed

# --- Set up the game window ---
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)              # Turn off auto screen updates for smooth animation
screen.bgcolor("black")

# --- Keyboard controls (event-driven programming) ---
screen.listen()
screen.onkeypress(snake.left1, 'a')   # Move left
screen.onkeypress(snake.right1, 'd')  # Move right
screen.onkeypress(snake.up1, 'w')     # Move up
screen.onkeypress(snake.down1, 's')   # Move down

# --- Main game loop ---
n = 0.1                # Initial speed (delay between moves)
game_is_on = True      # Game state flag

while game_is_on:
    screen.update()    # Refresh the screen manually
    time.sleep(n)      # Control the speed of the game
    snake.move()       # Move the snake forward (DSA: list shifting)

        # --- Check if snake eats the food (collision detection) ---
    if snake.segments[0].distance(food.tim.pos()) < 15:
        food.refresh()         # Place food at a new random location (DSA: randomization)
        snake.extend()         # Add a new segment to the snake (DSA: dynamic list growth)
        score1.scores += 1     # Increase the score
        score1.update_score()  # Update the score display
        n = n - 0.005         # Speed up the game a little

    # --- Check for collision with wall (boundary check) ---
    if (snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or 
        snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290):
        game_is_on = False
        score1.end_game2()     # Show game over message

    # --- Check for collision with itself (self-collision) ---
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 5:
            game_is_on = False
            score1.end_game1() # Show game over message



screen.mainloop()  # Keep the window open until closed by the user