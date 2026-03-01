class employee:
    company="ITC"
    name='defalut name'
    def show(self):
        print(f'the name is {self.name}and the salary{self.company}')

# class programmer:
#     company="ITC infotech"
#     def show(self):
#         print(f'the name is {self.name} and the salary is {self.salary}')

#     def showLanguage(self):
#         print(f'the name is {self.name} and he is good with { self.language} language')

class coder:
    language="python"
    def peintlang(self):
        print(f'print language{self.language}')


class programmer(employee,coder):
    company="ITC infotech"
    def showLangauage(self):
        print(f'the name is self {self.company} and he good whit {self.language}')
    

a=employee()
b=programmer()

b.show()
b.peintlang()
b.showLangauage()

print(a.company,b.company,b.language)


# Multilevel inheritance
class emp:
    a=1
class pro(emp)   :
    b=2
class man(pro):
    c=3
o=emp
print (o.a) # prints the a attribute
# print(o.b)   shows an error as there is no b attribute in 
            # employee class
o=pro()
print(o.a,o.b,o.c)



# super methos 

class employee:
    def __init__(self):
        print('constructor of employee')
    a=1
class programmer(employee):
    def __init__(self):
        print('constructor of programmer')
    b=2
class manager(programmer):
    def __init__(self):
        super().__init__()
        print('constructor of manager')
    c=3

o=manager()
print(o.a,o.b,o.c)



# Class method 





class employee:
    a = 1
    @classmethod
    def show(se):
        print(f'the value{se.a}')
e=employee()
e.a = 45
e.show()



# Property decoroters
class employee:
    a= 1 
    @classmethod
    def show(cls):
        print('show',cls.a)

    @property
    def name(self):
        return f'{self.fname} {self.lname}'
    
    @name.setter 
    def name(self,value):
        self.fname = value.split(' ')[0]
        self.lname = value.split(' ')[1]
e=employee()
e.a=45

e.name='sagar kondke'
print(e.fname,e.lname)
e.show()


# operator oveloading 

class number:
    def __init__(self,n):
        self.n=n
    def __add__(self,num):
        return self.n+num.n

n= number(1)
m=number(2)
print(n+m)
