# Integers and floats are the primary numeric data types in 
# Python. With them, you can store numeric data and 
# perform mathematical operations.

my_int= 56
print(type(my_int))


my_float1 =5.4
my_float2= 12.0
float_sub =my_float1 * my_float2
print (float_sub)



# How Do Augmented Assignments Work?

# Augmented assignment combines a binary operation
#  with an assignment in one step. It takes a variable, 
# applies an operation to it with another value, and
#  stores the result back into the same variable.

my_var =10
my_var +=5
print(my_var)


# How Do Conditional Statements 
# and Logical Operators Work?

#Conditional statements, or conditionals, let you
#  control the flow of your program based on whether 
# certain conditions are true or false

#  Conditional Statements 
# if condition:
    # pass # Code to execute if condition is True
age= 1
if age >= 18:
    print('you are adult')
elif age>13:
    print('you are a teenager')
elif age>=15:
    print ('you are also teen ager')
else:
    print('you are not an adult yet')


# What Are Truthy and Falsy Values, and How Do Boolean 
# Operators and Short-Circuiting Work?

print(bool(False))
print(bool(0))
# True
print(bool(True)) 
print(bool(1))

# There are three Boolean 
# operators in Python: and, or, and not.

is_citizen = True 
age=25
if is_citizen and age >=18:
    print('eligible to vote')
else:
    print('not eligible to vote')

    # OR
age =19
is_emp =True
if age <= 19 or is_emp:
    print('you are eligible')
else:
    print('your not eligible')

    # NOT
is_admin= False
if not is_admin:
    print('acced denied')
else:
    print('welcome')

    