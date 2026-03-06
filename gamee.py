# We all have played snake, water gun game in our childhood.
# If you haven’t, google the 
# rules of this game and write a python program 
# capable of playing this game with the 
# user. 




import random
'''
1 for snake
-1 for water
0 for gun

'''
import pandas as pd


computer=random.choice([-1,0,1])
youstr=input('inter your choic: ')
youDict={'s':1,'w':-1,'g':0}
reversDict={1:'snake',-1:'water',0:'Gun'}

you=youDict[youstr]

print(f'you chose{reversDict[you]}\nCmputer chose{reversDict[computer]}')

if(computer ==you):
    print('Its a draw')


else:
    if(computer ==-1 and you==1):
        print('you Win!')
    elif(computer ==1 and you==0):
        print('you Lose !')
    elif(computer==0 and you==-1):
        print('you lose !')
    elif(computer==1 and you==0):
        print('you lose !')
    elif(computer==0 and you==-1):
        print('you winn !')
    elif(computer==0 and you==1):
        print('you lose !')
    else:
        print('something went wrong')   

