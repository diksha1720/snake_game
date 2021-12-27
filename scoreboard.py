from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal ")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_data()
        print(self.high_score)
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()

    def read_data(self):
        with open("data.txt") as file:
            content = file.read()
            return int(content)

    def update_scoreboard(self):

        self.clear()
        self.write(f"Score: {self.score} Highest Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()


