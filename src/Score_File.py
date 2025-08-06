from turtle import Turtle

class score_bd(Turtle):
    def __init__(self):
        super().__init__()
        self.scores = 0  # DSA: Counter/Accumulator to keep track of the score
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 280)  # Place the score display at the top of the screen
        self.update_score()  # Show the initial score

    def update_score(self):
        self.clear()  # DSA: Overwrite previous score (reset display)
        # DSA: Output formatting, using the score as a variable
        self.write(f"Score: {self.scores*10}", align="center", font=("Seoge"))

    def end_game1(self):
        self.goto(0,0)      # Move to center for game over message
        self.clear()        # Clear previous score
        # DSA: Output final score and reason for game over (self-collision)
        self.write(
            f"Game Ended ! Score: {self.scores*10}\nSnake Died by Biting Itself *** ",
            align="center", font=("Seoge",24)
        )

    def end_game2(self):
        self.goto(0,0)      # Move to center for game over message
        self.clear()        # Clear previous score
        # DSA: Output final score and reason for game over (wall collision)
        self.write(
            f"Game Ended ! Score: {self.scores*10}\nOuch, Snake Died by Hitting the wall !",
            align="center", font=("Seoge",24)
        )