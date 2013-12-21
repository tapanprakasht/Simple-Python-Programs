#!/usr/bin/python3
# Simple calculator program in Python

class Calc:
  def __init__(self):
    self.num1=0
    self.num2=0
  def getNumber(self):
    self.num1=int(input("Enter the first number:"))
    self.num2=int(input("Enter the second number:"))
    
  def showMenu(self):
    print("\nSimple Calculator\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Exit")
    
  def findSum(self):
    return self.num1+self.num2
  
  def findDiff(self):
    return self.num1-self.num2
  
  def findMul(self):
    return self.num1*self.num2  
  def findDiv(self):
    return self.num1/self.num2
  
def main():
  c=Calc()
  c.showMenu()
  choice=int(input("Enter your choice:"))
  while choice!=5:
    
    c.getNumber()
    if choice==1:
      print("{} + {} = {}".format(c.num1,c.num2,c.findSum()))
    elif choice==2:
      print("{} - {} = {}".format(c.num1,c.num2,c.findDiff()))
    elif choice==3:
      print("{} * {} = {}".format(c.num1,c.num2,c.findMul())) 
    elif choice==4:
      print("{} / {} = {}".format(c.num1,c.num2,c.findDiv())) 
    c.showMenu()
    choice=int(input("Enter your choice:")) 
    
if __name__=="__main__":main()