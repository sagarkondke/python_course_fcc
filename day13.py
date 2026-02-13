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
def goodDay(name,ending):
    print('Good Day',name)
    print(ending)
goodDay('sagar','thank you')
goodDay('divya','Thanks')


# Return value 
def greet (name):
    gr='hello'+name
    return gr
a=greet('harry')
print(a)


# Default Parameter value 
# we can have a value as default as default 
# argument in function 


def gooday(name,ending='sagar'):
    print(f'good day,{name},{ending}')
gooday('day')


# ###
###          RECURSION  #######

def facto(n):
    if (n==1 or n==0):
        return 1
    return n* facto(n-1)

n = int (input('enter a number '))
print(facto(n))