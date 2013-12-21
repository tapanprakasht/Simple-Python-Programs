#!/usr/bin/python3
# Program to find prime numbers in range

class Prime:
  def __init__(self):
    self.limit=0
  def getLimit(self):
    self.limit=int(input("Enter the limit:"))
  def findPrimeNumbers(self):
    print("Prime numbers are")
    for i in range(2,self.limit+1):
      count=0
      for j in range(1,i+1):
	if i%j==0:
	  count=count+1
      if count==2:
	print(i)
	
def main():
  p=Prime()
  p.getLimit()
  p.findPrimeNumbers()
  
if __name__=="__main__":main()