#/usr/bin/python
#date:06/10/2013

class Parent:
  def myMethod(self):
    print "I am in parent class"
class Child(Parent):
  def myMethod(self):
    print "I am in child class"
    
pa=Parent()
pa.myMethod()
ch=Child()
ch.myMethod()