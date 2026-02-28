# constructor

class saga:
    sal=90000
    lag='py'

    def __init__(self,name ,sal,lag): # as dunder method witch is atuomactically called
        self.name=name
        self.sal=sal
        self.lag=lag
        
        print('i am crating an object')



    @staticmethod
    def greet():
        print('you will get job in deloitte')
harry=saga( 'harry',1400000,'javaScript')
harry.name='sagar'
print(harry.sal,harry.name,harry.lag)



# create a class 'programmer' for storing information
#  of few progrmmer working at microsoft


class programmer():
    company='microsoft'
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin
        
saga=programmer('sagar',1000000, 41007)
print(saga.name,saga.salary,saga.pin,saga.company)

r=programmer('rohan',1000000, 41007)
print(r.name,r.salary,r.pin,r.company)


# write a class 'calculator' capable of finding square,
# cube and square root of a number
class calculator():
    def __init__(self,s):
        self.s=s
    def square(self):
        print(f'the square {self.s*self.s}')
    def cube(self):
        print(f'the cube{self.s*self.s*self.s}')
    def squareroot(self):
        print(f'the squareroot{(self.s**1/2)}')
    
s=calculator(4)
s.square()
s.cube()
s.squareroot()


# 3. Create a class with a class attribute a; create 
# an object from it and set ‘a’ 
# directly using ‘object.a = 0’. Does this change 
# the class attribute? 
class demo:
    a=4
o=demo()
print(o.a)
o.a=0
print(o.a)
print(demo.a)


# 4. Add a static method in problem 2, to greet the 
# user with hello. 


class calculator():
    def __init__(self,s):
        self.s=s
    def square(self):
        print(f'the square {self.s*self.s}')
    def cube(self):
        print(f'the cube{self.s*self.s*self.s}')
    @staticmethod
    def say():
        print('say hello')

    def squareroot(self):
        print(f'the squareroot{(self.s**1/2)}')
    
s=calculator(4)
s.square()
s.cube()
s.squareroot()
s.say()

# Write a Class ‘Train’ which has methods to book 
# a ticket, get status (no of seats) 
# and get fare information of train running 
# under Indian Railways.

class train:
    def __init__(self,bt,gst,ginf,info):
        self.bt=bt
        self.gst=gst
        self.ginf=ginf
        self.info=info
t=train('yes','book',1230,'indianrailway')
print(t.bt,t.ginf,t.gst,t.info)

# second method
import random
class Train:
    def __init__(self,trainNO):
        self.trainNO=trainNO
    def book(self,fro,to):
        print(f'Ticket is booked in train no:{self.trainNO}from{fro} to{to}')
    def getstatus(self):
        print(f'trian no {self.trainNO} is running on time')
    def getFare(self,fro,to):
        print(f'Ticket is fare in train no:{self.trainNO} from {fro} to{to} is{random.randint(1,555)}')
t=Train(12399)
t.book('Rampur','delhi')
t.getstatus()
t.getFare('ramput','delhi')


# 6. Can you change the self-parameter inside 
# a class to something else (say 
# “harry”). Try changing self to “slf” or 
# “harry” and see the effects. 

class demo:
    def __init__(slf,hello):
        slf.hello=hello
d=demo('sagar')
print(d.hello)