#/usr/bin/python3
# Program to print the fibonnaci series

class Fibonacci:
  def __init__(self):
    self.a=0
    self.b=1
    self.c=0
    self.count=0
  def getCount(self):
    self.count=int(input("Enter the limit:"))
  def printSeries(self):
    n=1
    print("Fibonnaci series is ")
    while n<=self.count:
      print(self.a,end=' ')
      self.c=self.a+self.b
      self.a=self.b
      self.b=self.c
      n=n+1
    print("")
def main():
  f=Fibonacci()
  f.getCount()
  f.printSeries()
  
if __name__=="__main__":main()