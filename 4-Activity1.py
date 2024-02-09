"""
Group number: 4

Student 1: Narimaan Samani (UID: 754005820)
Student 2: Ala'a Al Zein (UID: 759009741) 
Student 3: Youssef Abdelfattah (UID: 405008858)
Student 4: Ayman Abdulwahid (UID: 405008855)

"""
from turtle import Turtle, Screen #importing turtle module

x = int(input('Enter a value between "-200, 150" for your initial "x" position for drawing: ')) #Input commands that the user will choose the drawing's "X" position
y = int(input('Enter a value between "-50, 100" for your initial "y" position for drawing: ')) #Input commands that the user will choose the drawing's "Y" position

#Function for setting position
def set_position(turta,x,y):
    """
    This function allows you to set the position that the user wants for the drawings
    """
    turta.penup()
    turta.goto(x,y)

#Initial function to draw the hexagon sizes
def hexagon(turta, forward, right):
    turta.forward(forward)
    turta.right(right)
    
#Function for drawing the hexagon
def hexagon_main(turta,shape_border_color,hexa_color):
    """
    This function is for drawing the hexagon
    """
    turta.pensize(2)
    turta.penup()
    turta.pencolor(shape_border_color)
    turta.pendown()
    turta.fillcolor(hexa_color)
    turta.begin_fill()

    hexagon(turta,50,60)
    hexagon(turta,50,60)
    hexagon(turta,50,60)
    hexagon(turta,50,60)
    hexagon(turta,50,60)
    hexagon(turta,50,60)

    turta.end_fill()        
    turta.penup()


#Function for drawing circle
def circle_main(turta,shape_border_color,circle_color):
    """
    This function is for drawing the circle
    """
    turta.pensize(2)
    turta.penup()
    turta.pencolor(shape_border_color)
    turta.right(90)
    turta.pendown()
    turta.fillcolor(circle_color)
    turta.begin_fill()
    
    turta.circle(45)
    
    turta.end_fill()
    turta.penup()

#Initial function to draw the hexagon sizes
def square(turta, forward, right):
    turta.forward(forward)
    turta.right(right)
    
#Function for drawing square
def square_main(turta,shape_border_color,square_color):
    """
    This function is for drawing the square
    """
    turta.right(90)
    turta.pensize(2)
    turta.penup()
    turta.pencolor(shape_border_color)
    turta.pendown()
    turta.fillcolor(square_color)
    turta.begin_fill()
    
    square(turta,90,90)
    square(turta,90,90)
    square(turta,90,90)
    square(turta,90,90)
        
    turta.end_fill()
    turta.penup()

#Main function to call everthing that we want to be run in the code
def main():
    shape_border_color = input("Enter your shape border color: ") #Input for the user to choose the border colors
    hexa_color = input("Enter your hexagon color: ") #Input command for the user to choose color of the hexagon
    circle_color = input("Enter your circle color: ") #Input command for the user to choose the color of the circle
    square_color = input("Enter your square color: ") #Input command for the user to choose the color of the square

    #This function draws all the shapes in a specific order.
    def Pattern(turta,x,y):
        """
        This function is for positioning and drawing the shapes based on the positions that the user entered at the beginning of the code
        """
        #Hexagon 1
        turta.penup()
        turta.goto(x,y)
        hexagon_main(turta,shape_border_color,hexa_color)

        #Circle 1
        turta.penup()
        turta.goto(x+100,y-50)
        circle_main(turta,shape_border_color,circle_color)
        
        #Square 1
        turta.left(180)
        turta.penup()
        turta.goto(x+220,y)
        square_main(turta,shape_border_color,square_color)
        
        #Hexagon 2
        turta.penup()
        turta.goto(x+70,y-120)
        hexagon_main(turta,shape_border_color,hexa_color)
        
        #Circle 2
        turta.penup()
        turta.goto(x+170,y-170)
        circle_main(turta,shape_border_color,circle_color)
        
        #Square 2
        turta.left(180)
        turta.penup()
        turta.goto(x+290,y-120)
        square_main(turta,shape_border_color,square_color)
        
        #Hexagon 3
        turta.penup()
        turta.goto(x+140,y-240)
        hexagon_main(turta,shape_border_color,hexa_color)
        
        #Circle 3
        turta.penup()
        turta.goto(x+240,y-290)
        circle_main(turta,shape_border_color,circle_color)
        
        #Square 3
        turta.left(180)
        turta.penup()
        turta.goto(x+360,y-240)
        square_main(turta,shape_border_color,square_color)
    
    #Calling the fuction "Pattern"
    Pattern(turta,x,y)
    
    turta.speed(5) #Set the drawing speed of the turtle to 5.
    
    wind = Screen() #Create a Screen object and assign it to the variable 'wind'.
    wind.exitonclick() #Wait for a click on the screen, then close the window.

turta = Turtle()#Create a Turtle object and assign it to the variable 'turta'.
turta_screen = Screen() #Also, create a Screen object and assign it to the variable 'turta_screen'


#Calling the function "main"
main()