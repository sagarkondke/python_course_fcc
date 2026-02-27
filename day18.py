# instance vs class attribute


class Employee:
    language ='py'  #This is class attributes
    salary= 120000
harry=Employee()
harry.language='sagar'  #This is instance attribute
print(harry.language,harry.salary)



# Self method 
class Employee:
    language ='py'  #This is class attributes
    salary= 120000
    def getinfo(self):
        print(f'The language is {self.language}')

    def greet(self):
        print(f"the {self.salary}")

harry=Employee()
harry.language='sagar'  #This is instance attribute
print(harry.language,harry.salary)
Employee.getinfo(harry)
Employee.greet(harry)






# Static mehtod 

class employee:
    salary=30000
    language='python'

    @staticmethod
    def greet():
        print('good morning')

saga=employee()
print(saga.salary)
saga.greet()

