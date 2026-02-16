# File input output 
'''
a='a very log string with emails'


emails=[]


'''

f =open('file.txt') #open the file 
data =f.read() # f.read is basically read the file 
print(data)
f.close # f.close is close the file 


# how to write the file 

st='sagar like gaytri'
f=open('file.txt','w')
f.write(st)
f.close



# how read file and print single line 

f= open('file.txt','r')
# lines=f.readlines()
# print(lines,type(lines))
# f.close

f= open('file.txt','r')
line=f.readline()
while(line !=''):
    print(line)
    line=f.readline()
f.close()



# append the file 


st='sagar is rally like her\n '
f=open('file.txt','a')
f.write(st)
f.close()

# With statepmt in pyhon to open and read file

with open('file.txt') as f:
    print(f.read())