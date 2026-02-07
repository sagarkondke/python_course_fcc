# Conditional Expression/ Statements 

# if elif else ladder 

a =int(input("enter you age "))
# if statement no :1
if(a%2 ==0):
    print('a is even')
# if statement no : 2
if(a>=18):
    print("you can drive")
    print('Good for you')
elif(a<0):
    print("you are entering invalid age")
elif(a==0):
    print('you are entering 0 which is not valid age')
else:
    print('you are below age of concent')
# end of if steaemt no 2 

# write a program to find thr freatest of four numbers
# entered by the user 
a=int(input('enter a number '))
b=int(input('enter a number '))
c=int(input('enter a number '))
d=int(input('enter a number '))
if (a>b and a>c and a>d) :
    print("print grater then ",a)
elif(b>a and b>c and b>d):
    print('greatest number is b',b)
elif(c>a and c>b and c>d):
    print('print the gratest number',c)
elif(d>a and d>b and d>c):
    print('print gratest nuber', d)

