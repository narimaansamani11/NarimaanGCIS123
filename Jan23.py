
#Make a chat bot
a = input("Hello this GPT, how may i assist you?")
b = input("Alright for this you can visit this website by clicking on the link below")
print(b)


#How to print pyramid
a = "   *   "
b = "  ***  "
c = " ***** "

print(a)
print(b)
print(c)


#Checking valid and invalid variables
_name = "Mike"
print(_name) #Valid

'''
1age = 10
print(1age) #invalid

my.variable = "Hello"
print(my.variable) #Valid
'''

VAR_NAME = "True"
print(VAR_NAME) #Invalid


#Using input an variable together
name = input("What's your name?")
print("Hello", name,"!")


#Code to write Happy Birthday
name = input("What's your name?")
month = input("What's your birth month?")
day = input("What's your birth day?")
year = input("What's your birth year?")

print("Your birthday is on", month, day, year,"!")





#use function for research paper
def TakeResearchPaper(count):
    ResearchPaper1 = input("Name your research paper: ")
    print("Research Paper", count,":", ResearchPaper1)

count = 1
TakeResearchPaper(count)
count +=1
TakeResearchPaper(count)
count +=1
TakeResearchPaper(count)


#use function for research paper (two variables), addition
def add(number1,number2):
    print(number1 + number2)
    
number1 = 10
number2 = 20

add(number1,number2)


#use function for research paper (two variables), dividion
def div(num1,num2):
    print(num1/num2)
    
num1 = 12
num2 = 2

div(num1,num2)


#use function for research paper (two variables), using return
def division(numb1,numb2):
    result = numb1/numb2
    return result

numb1 = 12
numb2 = 2

ReturnedResult = division(numb1,numb2)
print(ReturnedResult)


#use function for research paper (two variables), remainder
def remainder(no1,no2):
    result2 = no1 % no2
    return result2

no1 = 10
no2 = 5

ReturnedResult2 = remainder(no1,no2)
print(ReturnedResult2)


'''
pi = 3.14    #Float
pi = "3.14"  #String
'''

