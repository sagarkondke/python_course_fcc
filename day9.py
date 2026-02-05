#  dictionary is collection of the unique key_value pairs
# while 
# SET
# is an unorders collection of unique elements.




marks ={
    'sagar':89,
    'shubham':45,
    'sachin':33
}
print(marks.items())
print(marks.keys())
print(marks.values())

marks.update ({'sagar':88,'Renuka':99})
print(marks)

print(marks.get('sagar'))
print(len(marks))

# marks.pop('sagar') # its remove the items on dictionary
# print(marks)

# marks.popitem() #its remove lst item on ls dictionary 
# print(marks) 

