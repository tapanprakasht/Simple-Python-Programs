#!/usr/bin/python3
# Program to find the reverse of number 
class Reverse:
  def __init__(self):
    self.number=0
    
  def getNumber(self):
    self.number=int(input("Enter a number:"))
    
  def findReverse(self):
   rev=0
   mod=0
   num=self.number
   while num > 0:
      mod=num%10
      rev=rev*10+mod
      num=num//10
   print("Reverse of the number = {}".format(rev))

def main():
  r=Reverse()
  r.getNumber()
  r.findReverse()
  
if __name__=="__main__":main()
