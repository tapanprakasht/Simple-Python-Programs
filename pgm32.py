#!/usr/bin/python3.3
#Author:Tapan Prakash T
#Date:06/10/2013

try:
   fh=open("testfile","w")
   fh.write("Hello world")
except IOError:
   print 'error'
else:
   print "Success"
   fh.close()

