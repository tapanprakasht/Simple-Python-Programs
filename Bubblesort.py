#!/usr/bin/python3
class BubbleSort:
  def __init__(self):
    self.x=[]
    self.limit=0
    
  def getElements(self):
    self.limit=int(input("Enter the limit:"))
    print("Enter {} number".format(self.limit))
    for i in range(1,self.limit+1):
      self.x.append(int(input()))
  
  def sort(self):
    for i in range(0,self.limit):
      for j in range(0,(self.limit-1)-i):
	if self.x[j+1] < self.x[j]:
	  temp1=self.x[j+1]
	  temp2=self.x[j]
	  del self.x[j]
	  del self.x[j+1]
	  self.x.insert(j+1,temp2)
	  self.x.insert(j,temp1)
	  print(self.x)
    print("Sorted list is")
    for i in self.x:
       print(i)
       
       
def main():
  b=BubbleSort()
  b.getElements()
  b.sort()
if __name__=="__main__":main()