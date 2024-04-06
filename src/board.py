from turtle import Turtle


class Board(Turtle):
    def __init__(self, width, height):
        super().__init__(visible=False)
        self.width = width
        self.height = height
        self.print_board()

    def print_board(self):
        """Print a board game with 90% of the total screen size"""

        self.penup()
        self.color("lime")
        self.goto(int(self.width * -.45), int(self.height * -.45))
        self.pendown()

        for _ in [90, 0, 270, 180]:
            self.setheading(_)
            if _ == 90 or _ == 270:
                self.forward(int(self.height * .9))
            else:
                self.forward(int(self.width * .9))
