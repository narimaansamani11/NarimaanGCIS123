'''
#How to draw a smily face
from turtle import Turtle, Screen


def Face(turta,x,y,radius,color,pencolor):
    turta.up()
    turta.goto(x,y)
    turta.pencolor(pencolor)
    turta.down()
    turta.begin_fill()
    turta.fillcolor(color)
    turta.circle(radius)
    turta.end_fill()
    
def Nose(turta,x,y,radius,color,pencolor):
    turta.up()
    turta.goto(x,y)
    turta.pencolor(pencolor)
    turta.down()
    turta.begin_fill()
    turta.fillcolor(color)
    turta.circle(radius)
    turta.end_fill()
    
def Eye_1(turta,x,y,radius,color,pencolor):
    turta.up()
    turta.goto(x,y)
    turta.pencolor(pencolor)
    turta.down()
    turta.begin_fill()
    turta.fillcolor(color)
    turta.circle(radius)
    turta.end_fill()
    
def Eye_2(turta,x,y,radius,color,pencolor):
    turta.up()
    turta.goto(x,y)
    turta.pencolor(pencolor)
    turta.down()
    turta.begin_fill()
    turta.fillcolor(color)
    turta.circle(radius)
    turta.end_fill()
    
def Smile(turta,x,y,radius,color,pencolor):
    turta.up()
    turta.goto(x,y)
    turta.pencolor(pencolor)
    turta.down()
    turta.begin_fill()
    turta.fillcolor(color)
    turta.right(90)
    turta.circle(radius,180)
    turta.end_fill()
    
def main():
    wind = Screen()
    t = Turtle()
    t.pensize(3)
    t.speed(10)
    t.hideturtle()

    Face(t,0,0,90,"yellow","black")
    Nose(t,0,75,13,"red","red")
    Eye_1(t,33,115,11,"blue","blue")
    Eye_1(t,-33,115,11,"blue","blue")
    Smile(t,-40,60,40,"black","black")

    wind.exitonclick()
    
main()
'''


#How to draw a smiley face usingg another way (Mehtab way)

from turtle import Turtle, Screen #write before code

def position_func(turta):
    print(turta.xcor)
    print(turta.ycor)

def draw_circle(turta, x, y, radius, color):
    turta.up()
    turta.goto(x,y)
    turta.down()
    turta.begin_fill()
    turta.fillcolor(color)
    turta.circle(radius)
    turta.end_fill()

def draw_nose(turta, x, y, radius, color):
    turta.up()
    turta.goto(x,y)
    turta.down()
    turta.begin_fill()
    turta.fillcolor(color)
    turta.circle(radius)
    turta.end_fill()

def draw_eyes(turta, x, y, radius, color):
    turta.up()
    turta.goto(x,y)
    turta.down()
    turta.begin_fill()
    turta.fillcolor(color)
    turta.circle(radius)
    turta.end_fill()
    
def draw_smile(turta, x, y, radius, angle, color, radius2):
    turta.up()
    turta.goto(x,y)
    turta.down()
    turta.begin_fill()
    turta.fillcolor(color)
    turta.right(90)
    turta.circle(radius,angle)
    turta.end_fill()
    turta.left(90)
    turta.forward(radius2)

def main():
    wind = Screen()
    t = Turtle()
    t.speed(10)
    draw_circle(t, 0, 0, 100, "yellow") #pass through calling the values
    draw_nose(t, 0, 80, 10, "orange")
    draw_eyes(t,-40, 120, 15, "white")
    draw_eyes(t,40, 120, 15, "white")
    draw_eyes(t,-42, 122, 10, "blue")
    draw_eyes(t,42, 122, 10, "blue")
    draw_eyes(t,-41, 123, 6, "black")
    draw_eyes(t,41, 123, 6, "black")
    draw_smile(t, -28, 45, 30, 180, "white", 60)
    wind.exitonclick()

main()