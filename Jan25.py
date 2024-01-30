'''
#Return function
def add (a,b):
    result = a + b
    return result

a = 6
b = 4
c = add(6,4)

def subtract(c):
    return c - 9

d = subtract(c)

print(d)
'''


#How to add function using input:
def add (a,b):
    return a + b

a = int(input("Enter value 1 : ")) #This will make the value you enter be used as a number to be added or multiplied
b = int(input("Enter value 2 : ")) 

def add(a,b):
    return a + b
    
def subtract(a,b):
    return a - b

def division(a,b):
    return a / b

def multiply(a,b):
    return a * b
    
f = add(a,b)
g = subtract(a,b)
h = int(division(a,b))
i = int(multiply(a,b))

def main():
    print("Your added value is: ", f)
    print("Your subtracted value is: ", g)
    print("Your divided value is ", h)
    print("Your multiplied value is: ", i)
    
main()