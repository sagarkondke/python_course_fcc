# Functions and Recursions 
def avg():
    a=int(input('enter your number'))
    b=int(input('enter your number'))
    c=int(input('enter your number'))
    avegrage=(a+b+c)/3
    print(avegrage)
avg()

# Q1 write a program to greet a user with "good day" 
# using function

def greet():
    a=input('what is yor name ')
    print("have a good day",a)
greet()


# Function with argument
def goodDay(name):
    print('Good Day',name)
goodDay('sagar')