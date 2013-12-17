#!/usr/bin/python3
class Student:
  def __init__(self,name):
    self.name=name
  def printName(self):
    return self.name

def main():
  s1=Student("Tapan")
  s2=Student("mdga")
  print(s1.name)
  print(s2.name)

if __name__=="__main__": main()
