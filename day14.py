# ## Exercise of practice set

# Write a program using functions to find gratest
# of three numbers
# a=int(input('fitst num'))
# b=int(input('second num'))
# c=int(input('third num'))
def gretofthree(a,b,c):
    if (a>b and a>c):
         print(" A is grater")
    elif(b>a and b>c):
        print("B is grater")
    elif(c>b and c>a):
        print("c is grater")
gretofthree(4,5,6)


# Q2 Write a python program using function to convert 
# celsius to fahrenheit

# This is solve without argument passing 

def celsiusTofahr():
    f=int(input('enter temperature in F'))
    c=(f-32)*5/9
    print(c)
celsiusTofahr()

#second way to solve question
# this is solve to argument passing 

def c_TO_f(f):
    c=(f-32)*5/9
    return c
f=int(input('enter temperature in F'))
# round of is use to cut of the int 
print(round(c_TO_f(f),2))

# how do you prevent a python print()
# function to print a new line at the end

print('a')
print('b')
print('c',end='')
# end is prevent the they are not print in new line
print('d',end='')


# Write a recursive function to calculate the 
# sum of first natural numbers.
def sum_of_natural_numbes(n):
    if n==0:
        return 0
    else:
        return n+ sum_of_natural_numbes(n-1)
n=int(input('Take the natural numbers'))
print(sum_of_natural_numbes(n))

# Write a python function to print first  n lines of the
# following pattern:
def pat(n):
    for i in range (n,0,-1):      
        print("*"*i)
n=int(input('take the number'))
pat(n)


# second way to solve
def pattern(n):
    if(n==0):
        return
    print('*'*n)
    pattern(n-1)
pattern(5)

# write python function which converts inches to cms
def Inch_to_cm(inch,a):
    return inch*2.54
a=int(input('take the inche innpuut'))
print('Its in Centemeter',Inch_to_cm(a))

    
# doing this code without return 
def inchcm(inch):
    cm=inch*2.54
    print('its in cm',cm)
a=int(input('take the inch input'))
inchcm(a)


# Q7 write a python to remove a given word form a list
# ad strip it at the same time.

def rem(l,word):
    n=[]
    for item in l:
         if not(item==word):
             n.append(item.strip(word))
    return n
         
l=['sagar','rohan','prasad','saga','an']
print(rem(l,'an'))

# write a python function to print multiplication table
# of given number
def multipicationOftable(n):
    for i in range(1,11):
        print(i+n)
n=int(input('take a number'))
print(multipicationOftable(n))

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    result = [[i, j, k]
              for i in range(x + 1)
              for j in range(y + 1)
              for k in range(z + 1)
              if i + j + k != n]

    print(result)