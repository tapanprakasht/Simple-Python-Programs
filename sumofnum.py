#!/usr/bin/python3
# Program to find sum of numbers in the list
class SumOfNumber:
  def __init__(self):
    self.x=[]
    self.limit=0
    
  def getElements(self):
    self.limit=int(input("Enter the limit:"))
    print("Enter {} numbers".format(self.limit))
    for i in range(0,self.limit):
      self.x.append(int(input()))
  def findSumOfNumber(self):
    sum=0
    for i in range(0,self.limit):
      sum=sum+self.x[i]
    print("Sum of numbers in the list={}".format(sum))
   
def main():
  s=SumOfNumber()
  s.getElements()
  s.findSumOfNumber()
 
if __name__=="__main__":main()