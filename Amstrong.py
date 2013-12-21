#!/usr/bin/python3
# Program to check whether the given number is amstrong or not
class Amstrong:
  
  def __init__(self):
    self.num=0
    
  def getNumber(self):
    self.num=int(input("Enter the number:"))
    
  def checkNumber(self):
    n=self.num
    mod=0
    s=0
    while n>0:
      mod=n%10
      s=s+(mod*mod*mod)
      n=n//10
    if self.num == s:
      print("{} is an Amstrong number".format(self.num))
    else:
      print("{} is not an Amstrong number".format(self.num))
    
def main():
  a=Amstrong()
  a.getNumber()
  a.checkNumber()
  
if __name__=="__main__":main()
		 