#!/usr/bin/python
#Date:
class Employee:
  empCount=0
  
  def __init__(self,name,salary):
    self.name=name
    self.salary=salary
    Employee.empCount +=1
  def displayCount(self):
    print "Total number of employees is %d" %(Employee.empCount)
  def displayEmployee(self):
    print "Employee name:",self.name,"\nEmployee salary:",self.salary

def main():
  emp1=Employee("Tapan",30000)
  emp2=Employee("Anirudh",50000)
  emp1.displayEmployee()
  emp1.displayCount()
  print Employee.__module__
main()
