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


# Write a program to find out wheater a
# student has passed or failed if it required a total 
# 40% and at least 33% in each subject to pass assume 3 
# subject and take marks as a input from the user.


math=int(input("inter first sub mark"))
phy=int(input("enter second sub mark"))
che=int(input("enter third sub mark"))
total_percentage=(100*(math+phy+che))/300
if(total_percentage>40 and math>=33 and phy>=33 and che>=33):
    print('you are pass',total_percentage)
else:
    print('you are failed, try agian next year',total_percentage)



# Q3  A spam comment is defined as text containing following 
# Keywords:
# "make a lot of money".
# "Buy know", "subscribe this" , "ckick this"
# write a program to detect these spams,


p1='make a lot of money'
p2='Buy know'
p3="subscribe this"
p4="ckick this"
message=input("enter you message")
if ((p1 in message) or (p2 in message) or  (p3 in message) or (p4 in message)):
    print('this meassage is  spam')
else:
    print('its safe ')


# Q4 Write a program to find wheater a given 
# username contain less then 10 characer or not 

username=input('take the username')

if(len(username)>10):
    print('its contain more then 10 character ')
elif(len(username)<=10):
    print('its contain less then 10 character')


# Q5 write a program which finds out wheater a give
# username contains less then 10 character or not
li=['sagar','sachin','rohan','chaha']
name=input('take a input is present')
if(name in li ):
    print('its present')
else:
    print('its absent')

# #  Write a program to calculate the grade of a student from his marks from the 
# following scheme: 
# 90 – 100 => Ex 
# 80 – 90 => A 
# 70 – 80 => B 
# 60 – 70  =>C 
# 50 – 60 => D 
# <50 => F 

marks=int(input('Take input marks'))
if (marks<100 and marks>90):
    marks ='EX'
elif(marks<90 and marks>=80):
    marks ='A'
elif(marks<80 and marks>=70):
    marks='B'
elif(marks <70 and marks>=60):
    marks='C'
elif(marks <60 and marks>=50):
    marks='D'
elif(marks<50):
    marks='F'
print("your Grade is ", marks)


# Write a program to find out whether a 
# given post is talking a "harry or" not 
post=input('talking about to sagar')
p ='Sagar is not doing hard work i ' \
'am become making lazy'
if (post in p ):
    print('post is talking about sagar ')
else:
    print('its in not list')


        