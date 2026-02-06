s={1,3,5,7,9}

e= set() # as it will create an empty set 
# dont use s= {} it will create an empty dictionary 
print(type(e))

# sets method 

s={ 1, 3,5 ,6,7,4, 3,'sagar'}
print(type(s))

s.add('sakshi')
print(s)
s.remove(1)
print(s)
s.pop()
print(s)

# its UNION the can use to both sets same value can 
# be delets 
a={1,2,3,4,5,6}
b={1,2,7,8,9,9}
print(a.union(b))
print(a.intersection(b))

# practice sets 
# Q! Write a program to create a dictionary of hindi 
# words with values as Theri English translation.
# provides user with an option tool it up!. 

d={
    'hello':'kay chalu aahe',
    'getout':'baher ja',
    'myname':'maze nav '
    }
words=input('enter the word you want')
print(d [words])

# Q2 Write a program to input eight number from the user
# and display all the unique numbers(once)
s= set()
n=int(input('Take number input'))
s.add(n)
n=int(input('Take number input'))
s.add(n)
n=int(input('Take number input'))
s.add(n)
n=int(input('Take number input'))
s.add(n)
n=int(input('Take number input'))
s.add(n)
n=int(input('Take number input'))
s.add(n)
n=int(input('Take number input'))
s.add(n)
n=int(input('Take number input'))
s.add(n)
print(s)

# can we have a set with 18(int) '18'(str) 
# as a value in it ?
l= set()
l.add(18)
l.add('18')
print(l)

# what is be length of following set s
s =set()
s.add(20)
s.add(20.2)
print(len(s))

# s={}.
# what is the type of 's'?

s={}
print(type(s))

# create an empty dictinay. 
# Allow 4 Frinds to enter theri favorite language as value
# and use key as their names.
# Assume that the names are unique

a={}
b=int(input("input the value"))
c=input("input the key ")
a.update({b:c})

b=int(input("input the value"))
c=input("input the key ")
a.update({b:c})


b=int(input("input the value"))
c=input("input the key ")
a.update({b:c})

b=int(input("input the value"))
c=input("input the key ")
a.update({b:c})
print(a)


# if the names of two frineds are same; what will happen
# to the program in problem 6 ?
# ANS :- Dictionary is update the give new and second value


# can you change the values inside a list which is 
# contained in set s

s={ 8,7,12,'harry',[1,2]}
print(s)

# set is mutable 
