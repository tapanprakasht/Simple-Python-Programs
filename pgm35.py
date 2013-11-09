#/usr/bin/python
#date:06/10/2013

class Calc:
  def __init__(self,a,b):
    self.a=a
    self.b=b
  def add(self):
    print "Sum of ",self.a," and ",self.b," is ",self.a+self.b
  def sub(self):
    print "Difference of ",self.a," and ",self.b," is ",self.a-self.b

def main():
  print("Enter two numbers")
  num1=int(input())
  num2=int(input())
  cal1=Calc(num1,num2)
  cal1.add()
  cal1.sub()
main()