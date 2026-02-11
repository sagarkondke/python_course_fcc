# write a program to print 1 to 50 using while loops.
i =1
while (i<50):
    print(i)
    i+=1



# this is using the break statement 
for i in range (100):
    if(i==43):
        break #Exit the loop right now 
    print(i)

# there is use for the "Continue" here
for i in range(100):
    if(i==45):
        continue
    print(i)

# pass

for i in range(655):
    pass #pass is basically something is pass

i =0
while(i<45):
    print(i)
    i+=1

# Chapter 7 Practice SET
# 1. Write a program to print multiplication 
# table of a given number using for loop. 

n=int(input("take the table "))
i=1
while i<=10 :
    print(n*i)
    i+=1
    

n=int(input("take the table "))   
for i in range(1,11):
    print(i*n)


# Write a program to greet all the person names 
# stored in a list ‘l’ and which starts 
# with S. 
# l = ["Harry", "Soham", "Sachin", "Rahul"] 

l = ["Harry", "Soham", "Sachin", "Rahul"] 
for name in l:
    if(name.startswith('S')):
        print(f'hello {name}')

# Q 3 Attempt problem 1 using while loop 

n=int(input("Take the table"))
i=1
while i<=10:
    print(i*n)
    i+=1

# write a number to find wheater a given
# number is prine or not 
pn=int(input("Enter a number\n"))
i=0
while i<100:
    print(f'its prime number {i%2==0}')
i+=1


pn=int(input("Enter a number\n"))
for i in range(2,pn):
    if (pn %i  ==0):
        print('number is not prime')
        break
    else:
        print('its prime number')

# using while loop
pn=int(input("Enter a number\n"))
i=2
while i < pn:
    if pn%i==0:
        print('its prime not number')
        break
    i+=1
else:
    print('its prime number')

# write a program to find the sum of first n natural 
# numbers using while loop.
n=int(input("take the natural number "))
i=1
sum=0
while i<=n:
    sum+=i
    i+=1
    print(sum)
    
# Write a program to calculate the factorial of a 
# given number using For loop 
n=int(input("take the natural number "))
f=1
for i in range(1, n+1):
    f=f*i
    print(f)
    

# Write a program to print the following star pattern. 
# * 
# *** 
# ***** for n = 3
n=int(input("take the natural number "))
for i in range(1, n+1):
    print(" "* (n-i),end='')
    print("*" *(2*i-1),end='')
    print("")


# second star pattern 
for i in range (5):
    print("*****")
#  ANS
# *****
# *****
# *****
# *****
# *****


# third star pattern 
# *
# **
# ***
# ****
# *****

for i in range(1,5):
    print("*"* i)

# *****
# ****
# ***
# **
# *
# - minues pattern 
for i in range(5,0,-1):
   print("*"* i)

#     *
#    ***
#   *****
#  *******
# *********

for i in range(1,6):
    print(' '*(5-i) +'*' * +(2*i-1))






# 8. Write a program to print the following star pattern: 
# * 
# ** 
# ***      for n = 3 
n=int(input("take the natural number "))
for i in range(1,n):
    print("*" *i )



# 9. Write a program to print the following star pattern. 
# * * * 
# *   *   for n = 3 
# * * *  

n=int(input("take the number "))
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n,end='')
    else:
        print('*',end='')
        print(" "*(n-2),end='')
        print('*',end='')
    print('')
    
    # using for the most complex example solving  
n = 3

for i in range(n):
    for j in range(n):
        # Print star for first row, last row, first column, last column
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()



# 10. Write a program to print multiplication table of 
# n using for loops in reversed order. 


n=int(input("inter a number "))
for i in range (1,11):
    print(n*(11-i))