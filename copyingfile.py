#!/usr/bin/python3
# Program to copy content of one file to another

def main():
  infile =open('address.txt','r')
  outfile=open('new.txt','w')
  for line in infile:
    print(line,file=outfile,end='')
  print('Copying finished')
  
if __name__=="__main__":main()