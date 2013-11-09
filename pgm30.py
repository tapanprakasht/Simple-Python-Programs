text='''Hai I am Tapan Prakash.
I love programming.
I like Java,Python,Php programming.'''

f=open('tap.txt','w')
f.write(text)
f.close()

f=open('tap.txt')

while True:
    line=f.readline()
    if len(line)==0:
        break
    print(line,end='')
f.close()
