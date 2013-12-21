#!/usr/bin/python3
# Regular Expression-Find and replace 2

import re
def main():
  fh=open('address.txt')
  for line in fh:
    match=re.search('Ta',line)
    if match:
      print(line.replace(match.group(),'##'),end='')
      
if __name__=="__main__":main()