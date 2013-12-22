#!/usr/bin/python3
# Program to check the given string is palindrome or not
def main():
  str=input("Enter the string:")
  length=len(str)
  length=length-1
  i=0
  flag=True
  while i<=length:
    if str[i]!=str[length]:
      flag=False
      break
    i+=1
    length-=1
  if flag==False:
    print("{} is not palindrome".format(str))
  else:
    print("{} is palindrome".format(str))
 
if __name__=="__main__":main()