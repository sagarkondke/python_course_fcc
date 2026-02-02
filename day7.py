# Exercises 3

# Write a python program to display a user entered name 
# followed by good afternoon using input () function.
a = input('give to message ')
print("good afternoon ",a)

# Q2 write a program to fill in a letter 
# template given below with name and date 

letter='''Dear <|name>,
          you are selected!
          <|Date|>

'''
print (letter.replace("<|name>","sagar").replace("<|Date|>","24 sep 2090"))


# Q3 write a program to detect double space in a string 
name= "hello  sagar how are you  "
print(name.find("  "))


# Q4 Replace the double space form problem 3 with 
# single space
name= "hello  sagar how are you  "
a=(name.replace("  "," "))
print(a)


# write a program to format the following letter using 
# escape sequence characters.

letter = "dear Sagar,\nthis python course id nice.\nthnks"
print(letter)