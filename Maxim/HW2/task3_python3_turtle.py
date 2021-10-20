from turtle import *


Screen().setup(450, 450)

# main circle
penup()
setpos(0, -160)
pendown()
pen(fillcolor="yellow", pencolor="black", pensize=9)
begin_fill()
circle(160)
end_fill()


# eye
def eye(x: int, y: int) -> None:  # x, y coordinates of eye
    penup()
    setpos(x, y)
    pendown()
    pen(fillcolor="black", pencolor="black", pensize=3)
    begin_fill()
    seth(90)
    circle(35, 45)
    circle(10, 90)
    circle(35, 90)
    circle(10, 90)
    circle(35, 45)
    end_fill()


eye(-40, 50)  # left eye
eye(70, 50)   # right eye

# mouse
penup()
setpos(-60, -60)
pendown()
seth(-45)
pen(pencolor="black", pensize=9)
circle(90, 90)

hideturtle()
done()
