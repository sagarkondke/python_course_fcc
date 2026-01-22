# How Do Functions Work in Python?
# Functions are reusable pieces of code that run
#  when you call them. Many programming languages 
# come with built-in functions that make it easier 
# to get started. Python is no exception, and we've 
# already covered some built-in functions like print() 
# in previous lessons.

# Another helpful built-in function is input(), 
# which lets you prompt the user for input:

name= input('what is your name?')
print ('hello', name)

# On the other hand, int() converts a number, boolean, 
# and a numeric string into an integer:
print (int(3.1444))

# You can also write your own custom functions. 
# To do that, you use the '[def]' keyword,

def hello():
    print('hello world')
hello()

# simple function that prints the sum of two 
# numbers to the terminal:

def cal_sum (a,b):
    print(a+b)
cal_sum(4,6)

my_sum=cal_sum(6,6)
print(cal_sum)


def calcu(c,d):
    return c+d
my_cal=calcu(3,5)
print (my_cal)

# What Is Scope in Python and How Does It Work?

# In Python, scope determines the point at which you 
# can access a variable. It's what controls the lifetime 
# of a variable and ho
# w it is resolved in different parts of the code.

def my_fun():
    my_var=10
    print(my_var)
my_fun()


# Enclosing scope means that a function that's 
# nested inside another function can access the
#  variables of the function it's nested within

def outer_func():
    msg ='hello all'
    def inner_func():
        print(msg)
    inner_func()
outer_func()


# Global scope refers to variables that are declared 
# outside any functions or classes which can be
#  accessed from anywhere in the program

my_var=100
def show_var():
    print(my_var)
show_var()
print(my_var)