import random
n = random.randint(1,10)
a=-1
guesses=1
while (a!=n):
    a = int(input('guess the number:'))
    if(a>n):
        print('lower number please')
        guesses+=1
    elif(a<n):
        print('higher number please')
        guesses+=1
print(f'you have guessed the number {n} curectly in {guesses} attempts')

# thid project is really good and doing multiple enoyinh this 
