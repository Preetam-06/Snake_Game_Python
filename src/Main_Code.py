from turtle import Turtle, Screen
import time
from Snake_File import SnakeSegment
from Snake_Food_File import Food
from Score_File import score_bd,menu_bd

# --- Global Variables ---
snake = None
food = None
score1 = score_bd()
menu1 = menu_bd()
game_is_on = False
n = 0.1  # Speed
pause = False
rf=1

# --- Set up the game window ---
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)              # Turn off auto screen updates for smooth animation
screen.bgcolor("black")

# --- Main game function loop ---  

def game():
    global game_is_on,n,pause
    if game_is_on and pause == False:
        screen.update()    # Refresh the screen manually
        time.sleep(n)      # Control the speed of the game
        
        snake.move()       # Move the snake forward (DSA: list shifting)

        # --- Check if snake eats the food (collision detection) ---
        if snake.segments[0].distance(food.tim.pos()) < 15:
            food.refresh()         # Place food at a new random location (DSA: randomization)
            snake.extend()         # Add a new segment to the snake (DSA: dynamic list growth)
            score1.scores += 1 
            print(score1.scores*10)    # Increase the score
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
    if game_is_on:               
        screen.ontimer(game,rf)
            
# --- Start Game ---
def start():
    global snake, food, score1, game_is_on, n
    game_is_on = False  # stop any previous game loops
    pause = False
    
    screen.clear()
    screen.bgcolor("black")
    screen.tracer(0)

    # --- Create game objects ---
    snake = SnakeSegment()        # Our snake, which is a list of Turtle segments
    score1 = score_bd()           # Scoreboard (uses a Turtle for drawing text)
    menu1 = menu_bd()
    snake.create_snake(3)         # Start with 3 segments
    food = Food()                 # Food object, randomly placed
    n = 0.1
    rf=1
    game_is_on = True
    keys()
    game()
<<<<<<< Updated upstream
=======

def paused():
    global pause
    pause = not pause
    keys()
    

# --- Restart game ---
def restart():
    global game_is_on
    game_is_on = False
    start()

# --- Keyboard controls (event-driven programming) ---
def keys():
    screen.listen()
    screen.onkeypress(start,'space')
    screen.onkeypress(paused,'r')
    screen.onkeypress(restart,'Return')
    if snake:
        screen.onkeypress(snake.left1, 'a')   # Move left
        screen.onkeypress(snake.right1, 'd')  # Move right
        screen.onkeypress(snake.up1, 'w')     # Move up
        screen.onkeypress(snake.down1, 's')   # Move down
keys()
>>>>>>> Stashed changes

def paused():
    global pause
    pause = not pause
    keys()
    

# --- Restart game ---
def restart():
    global game_is_on
    game_is_on = False
    start()

# --- Keyboard controls (event-driven programming) ---
def keys():
    screen.listen()
    screen.onkeypress(start,'space')
    screen.onkeypress(paused,'r')
    screen.onkeypress(restart,'Return')
    if snake:
        screen.onkeypress(snake.left1, 'a')   # Move left
        screen.onkeypress(snake.right1, 'd')  # Move right
        screen.onkeypress(snake.up1, 'w')     # Move up
        screen.onkeypress(snake.down1, 's')   # Move down
keys()

screen.mainloop()  # Keep the window open until closed by the user
