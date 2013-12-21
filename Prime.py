#!/usr/bin/python3
class Prime:
  def __init__(self,num):
    self.number=num
  def findPrime(self):
    count=1
    for i in range(2,num+1):
      if self.number % i==0:
	 count=count+1
	
	
    if count==2:
      print("{} is prime".format(self.number))
    elif count>2:
      print("{} is not prime".format(self.number))
    else:
      print("{} is neither prime nor composite".format(self.number))
    return False
def main():
  num=int(input("Enter a number:"))
  p=Prime(num);
  p.findPrime()
  
if __name__=="__main__":main()