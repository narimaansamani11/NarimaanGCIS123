import turtle
'''
#How to draw a triangle
def Triangle():
    turtle.pendown()
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.penup()

def Cordinates():
    print(("X-Cordinates: "),turtle.xcor())
    print(("Y-Cordiantes: "),turtle.ycor())


#How to add a circle to the previous code
def Circle():
    turtle.pendown()
    turtle.circle(-35)
    turtle.penup()
    
    
#The main function
def main():
    Triangle()
    Circle()
    Cordinates()
    turtle.done()

main()   



#Making a student profile
def profile(a,b,c,d):
    info = a,b,c,d
    return info

def main():
    a = input("Enter your name: ")
    b = int(input("Enter your age: "))
    c = input("Enter your degree: ")
    d = bool(input("Are you a current student? Write 1 for YES and 2 for NO: "))
    print(profile(a,b,c,d))
        
    
main()
'''


#Making 3 squares in different sizes and different angles
angle = 90 

turtle.hideturtle()

def SetHeading1():
    turtle.setheading(20)

def SetHeading2():
    turtle.setheading(45)
    
def SetHeading3():
    turtle.setheading(70)
    
def Square1():
    turtle.pensize(3)
    turtle.pencolor("black")
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.forward(100)
    turtle.right(angle)
    turtle.forward(100)
    turtle.right(angle)
    turtle.forward(100)
    turtle.right(angle)
    turtle.forward(100)
    turtle.right(angle)
    turtle.end_fill()
    
def Square2():
    turtle.pensize(3)
    turtle.pencolor("black")
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.forward(75)
    turtle.right(angle)
    turtle.forward(75)
    turtle.right(angle)
    turtle.forward(75)
    turtle.right(angle)
    turtle.forward(75)
    turtle.right(angle)
    turtle.end_fill()


def Square3():
    turtle.pensize(3)
    turtle.pencolor("black")
    turtle.fillcolor("blue")
    turtle.begin_fill()
    turtle.forward(50)
    turtle.right(angle)
    turtle.forward(50)
    turtle.right(angle)
    turtle.forward(50)
    turtle.right(angle)
    turtle.forward(50)
    turtle.right(angle)
    turtle.end_fill()

    
def main():
    SetHeading1()
    Square1()
    SetHeading2()
    Square2()
    SetHeading3()
    Square3()
    turtle.done()
    
main()


#