import random

# practice set 

# Q1 write a program to read the text from a given file 
# 'poems.txt' and find out whether it contains 
# the word'twinkle'

f= open('poems.txt')
data=f.read()
print(data)
f.close()


# ex 2
f=open('poems.txt','r')
data=f.read()
if('Twinkal ' in data):
    print('the poen is write')
else:
    print('poen is not right')
f.close()



# # Q2 The game() function in a program lets a user 
# play a game and returns the score 
# as an integer. You need to read a file 
# ‘Hi-score.txt’ which is either blank or 
# contains the previous Hi-score. You need 
# to write a program to update the Hi
# score whenever the game() function breaks the Hi-score. 

def game():
    print('you are playing the game..')
    score=random.randint(1,50)
    # Fetch the hiscore
    with open('hiscore.txt') as f:
        hiscore=f.read()
        if(hiscore!=''):
            hiscore=int(hiscore)
        else:
            hiscore = 0
    print(f'your score:{score}')
    if(score>hiscore):
        with open('hiscore.txt','w') as f:
            f.write(str(score))
        return score
game()




# Q3 write a program to generate multipliaction table 
# from 2 to 20 and write it to the different files.
# please ther files in folder for 13 year old.

a=int(input("take a number "))
with open('file.txt','w') as f:
        for i in range(1,11):
            f.write(str(f'{a*i}\n'))
print(f'{a}')
f.close()

# Q4 A file contains a world "donkey" multiples times.
# you need to write a program which replace this world with
# "####" by updating the same file 

content=input('take input')
with open('file.txt','r') as f:
        content=f.read().replace(content,'####')
with open('file.txt','w')as f:
     f.write(content)
print(content) 


# 5. Repeat program 4 for a list of such words 
# to be censored. 

words=['donkey','gaytri','sonali']
with open('file.txt','r') as f:
     content=f.read()
for word in words: 
    content=content.replace(word,"#"*len(word))
with open('file.txt','w') as f:
     f.write(content)


# 6 Write a program to mine a log file and find out
#  whether it contains ‘python’. 
with open('file.txt','r') as f:
     a=f.read()
     if ('python' in a):
          print('yes it is present')
     else:
          print('its not present')


# Q7 write a program to find out the line number where 
# python is present from ques 6 .
with open('file.txt') as f:
     lines=f.readlines()
lineno=1
for line in lines:
     if('python' in line):
          print(f'yes its is present: {lineno}')
          break
     lineno+=1
else:
     print('no python is present')


# Q8 write a program to make a copy of a text file
# 'This.txt'

with open('file.txt') as f:
     content=f.read()
with open('thisf.txt','w') as f:
     content=f.write(content)
print(content)


# 9. Write a program to find out whether a file is identical & matches the content of 
# another file. 
with open ('file.txt','r') as f:
     content=f.read()
with open('gamee.py') as f:
     content2=f.read()
if content==content2:
     print('This is identical')
else:
     print('its not identical')




# 10. Write a program to wipe out the content of a
#  file using python. 
with open ('poems.txt','w') as f:
     f.write('')


# 11. Write a python program to rename a file 
# to “renamed_by_ python.txt. 


          
          
     

