#!/usr/bin/python3
# Regular Expression-Search and replace 1

import re
def main():
  fh=open('address.txt')
  for line in fh:
    print(re.sub('Ta','##',line),end='')

if __name__=="__main__":main()