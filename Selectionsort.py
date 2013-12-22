#!/usr/bin/python3
# Selection sort in python

class Selectionsort:
  def __init__(self):
    self.arr=[]
    self.count=0
    
  def getElements(self):
    self.count=int(input("Enter the limit:"))
    print("Enter {} elements".format(self.count))
    for i in range(0,self.count):
      self.arr.append(int(input()))
    print("Given list is")
    print(self.arr)
  
  def sort(self):
    for i in range(0,self.count):
      index=i
      for j in range(i+1,self.count):
          if self.arr[j]<self.arr[index]:
              index=j
      temp=self.arr[index]
      self.arr[index]=self.arr[i]
      self.arr[i]=temp
    print("Sorted list is ")
    print(self.arr)
      
    
def main():
  s=Selectionsort()
  s.getElements()
  s.sort()
  
if __name__=="__main__":main()
