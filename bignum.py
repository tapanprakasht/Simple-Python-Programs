#!/usr/bin/python3
# Program to find largest and smallest number in list
class BigNumber:
  def __init__(self):
    self.x=[]
    self.limit=0
    
  def getElements(self):
    self.limit=int(input("Enter the limit:"))
    print("Enter {} numbers".format(self.limit))
    for i in range(0,self.limit):
      self.x.append(int(input()))
      
  def getBignumber(self):
    big=self.x[0]
    small=self.x[0]
    for i in range(1,self.limit):
	if self.x[i] > big:
	  big=self.x[i]
	elif self.x[i]<small:
	  small=self.x[i]
    print("Current list={}".format(self.x))
    print("Largest Number in the list={}".format(big))
    print("Largest Number in the list={}".format(small))
    
    
def main():
  b=BigNumber()
  b.getElements()
  b.getBignumber()
  
if __name__=="__main__":main()
