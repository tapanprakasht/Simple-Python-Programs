#!/usr/bin/python3
# Regular Expressions-Precompiling patten
import re
def main():
  fh=open("address.txt")
  patten=re.compile('(Ta|Tha)')
  for line in fh:
    if re.search(patten,line):
      print(line,end='')

if __name__=="__main__":main()