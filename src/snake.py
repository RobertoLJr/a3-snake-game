from turtle import Turtle

INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []  # This is a list o Turtle objects
        self.create_snake()
        self.head = self.segments[0]
        self.head.color("green")
        self.last_input = 0

    def create_snake(self):
        """Create the snake character with the three segments determined by constant INITIAL_POSITIONS"""

        for position in INITIAL_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Create a new segment as a Turtle object and append it to this object's list of segments"""

        new_seg = Turtle("square")
        new_seg.color("lime")
        new_seg.penup()
        new_seg.goto(position)
        self.segments.append(new_seg)

    def extend(self):
        """Add the last segment from the object's list to the end of the snake character, regardless of current size"""

        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move all the segments from the snake character together"""

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        self.last_input = self.head.heading()

    def move_up(self):
        if self.last_input != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.last_input != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.last_input != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.last_input != LEFT:
            self.head.setheading(RIGHT)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.__init__()
