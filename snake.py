from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP_DIRECTION_ANGLE = 90
DOWN_DIRECTION_ANGLE = 270
LEFT_DIRECTION_ANGLE = 180
RIGHT_DIRECTION_ANGLE = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN_DIRECTION_ANGLE:
            self.head.setheading(UP_DIRECTION_ANGLE)

    def down(self):
        if self.head.heading() != UP_DIRECTION_ANGLE:
            self.head.setheading(DOWN_DIRECTION_ANGLE)

    def left(self):
        if self.head.heading() != RIGHT_DIRECTION_ANGLE:
            self.head.setheading(LEFT_DIRECTION_ANGLE)

    def right(self):
        if self.head.heading() != LEFT_DIRECTION_ANGLE:
            self.head.setheading(RIGHT_DIRECTION_ANGLE)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
