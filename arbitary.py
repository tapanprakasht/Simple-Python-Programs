#!/usr/bin/python3
# Arbitary arguments,Keyword arguments
def main():
  newFunction(1,2,3,46,one=1,two=2,three=3)
def newFunction(*arg,**kwargs):
  for i in arg:
    print(i,end=' ')
  for k in kwargs:
    print(k,kwargs[k])
  print('')
if __name__=="__main__":main()