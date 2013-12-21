#!/usr/bin/python3
def main():
  n=34
  print("Working with string examples")
  str="Hai,This is string"
  print(str)
  str2="Number={},Method 1".format(n)
  print(str2)
  str3="Number=%s,Method 2" %n
  print(str3)
  str4='''\
  first line
  second line
  third line'''
  print(str4)
  
if __name__=="__main__":main()
