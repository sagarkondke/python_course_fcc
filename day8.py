# Tuples in python 
# A tuples in pthon is immutable data type in python 
a = (1,3,5,6,7)
print(type(a))

no=a.count(5)
print(no)

n=a.index(5)
print(n)

print(len(a))

# write a program to store seven fruits in a list 
# entered by the user
fruits =[]
f1=input('enter the fruits name:')
fruits.append(f1)
f2=input('enter the fruits name:')
fruits.append(f2)
f3=input('enter the fruits name:')
fruits.append(f3)
f4=input('enter the fruits name:')
fruits.append(f4)
print(fruits)


# write a program accept marks of 6 students 
# and display them in a sorted manner.
stu_mark=[]
s1=input("first student mark")
stu_mark.append(s1)
s2=input("second student mark")
stu_mark.append(s2)
s3=input("third studnet mark")
stu_mark.append(s3)
stu_mark.sort()
print(stu_mark)

# check that tupple cannot be change in python
a = (34,234,'sagar')
a[2]='harry'
print(a)


# write a program to sum a list with 4 numbers

l=[32,33,34,46]
print(sum(l))


# write a program to count the 
# number of zeros in the following tuble 
a=(0,0,0,0)
print(a.count(0))


# day 9










