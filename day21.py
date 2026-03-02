# practice set 

# Q1 creat a class (2-D vector) and use ti to create another
# class representing a 3 D vector

class twoDvector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show (self):
        print(f'the vector is {self.i}i+{self.j}j')
class threeDvector(twoDvector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def show(self):
        print(f'the vector is {self.i}i+{self.j}j+{self.k}k')
a=twoDvector(1,2)
a.show()
b=threeDvector(1,2,3)
b.show()



# Create a class 'pet' from a class animal and furter
# create a class 'dog' form pets add a method bark to
#  class dog

class animal:
    pass
class pets(animal):
    pass
class dog():
    @staticmethod
    def bark():
        print('bow bow!')
a=dog()
a.bark()


# create a class Employee and add salary incremnt 
# properties to it

class Employee:
    salary=234
    increment=20
e=Employee()

# write a method salary aftr increment  method with a
# @property decorator with a setter which changes the value
# of increment based on the salary


class Employee:
    salary=234
    increment=20
    @property
    def salaryAfterIncrement(self):
        return(self.salary +self.salary* (self.increment /100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,salary):
        self.increment = ((salary/self.salary)-1)*100
e=Employee()
# print(e.salaryAfterIncrement)
e.salaryAfterIncrement= 280.8
print(e.increment)


# write a class complex to represent complex numbers,
# along with overloaded operators '+' and '*' which adds 
# and multiplies them

class complex:
    def __init__(self , r,i):
        self.r=r
        self.i=i

    def __add__(self,c2):
        return complex(self.r + c2.r,self.i+c2.i)
    
    def __str__(self):
        return f' {self.r}+{self.i}'
    
c1=complex(1,2)
c2=complex(3,4)
print(c1+c2)