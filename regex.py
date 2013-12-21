#!/usr/bin/python3
# Regular Expressions
import re
def main():
  fh=open("address.txt")
  for line in fh:
    if re.search('(Ta|Tha)',line):
      print(line,end='')

if __name__=="__main__":main()