from turtle import Turtle

starting_positions = [(0,0),(-20,0),(-40,0)]

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

        
    def create_snake(self):
        for pos in starting_positions:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(pos)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range (len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(20)
        screen_collision = self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor()>260 or self.head.ycor() < -280
        tail_collision = False
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 5:
                tail_collision = True
        if screen_collision or tail_collision:
            # over = Turtle()
            # over.color("red")
            # over.hideturtle()
            # over.penup()
            # over.goto(0,0)
            # over.write("Game Over!!!",align="center",font=("Courier new",18,"normal"))
            # print("Game Over")
            return False
        return True
        
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def extends(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def increase_speed(self):
        pass

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]