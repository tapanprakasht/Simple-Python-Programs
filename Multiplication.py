#!/usr/bin/python3

class Multiplication:
  def __init__(self):
    self.num=0
    self.count=0
  def getValues(self):
    self.num=int(input("Enter the number:"))
    self.count=int(input("Enter the count:"))
  def printMultTable(self):
    for i in range(1,self.count+1):
      print("{} X {} = {}".format(i,self.num,i*self.num))
      
def main():
  m=Multiplication()
  m.getValues()
  m.printMultTable()
  
if __name__=="__main__":main()
