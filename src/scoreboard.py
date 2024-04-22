from turtle import Turtle

FONT = ("Arial", 22, "normal")


class Scoreboard(Turtle):
    def __init__(self, screen_h):
        super().__init__(visible=False)
        self.screen_h = screen_h
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, int(self.screen_h * 0.45))

        # Open file with the highest score. If it doesn't exist, create one
        try:
            with open("./data.txt") as data:
                self.highest_score = int(data.read())
        except FileNotFoundError:
            with open("./data.txt", "w") as data:
                data.write("0")
                self.highest_score = 0
        finally:
            self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}          Highest Score: {self.highest_score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_scoreboard(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("./data.txt", mode="w") as data:
                data.write(f"{self.highest_score}")
        self.score = 0
        self.update_scoreboard()
