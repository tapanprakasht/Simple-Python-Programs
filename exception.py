#!/usr/bin/python3
try:
	fh=open("address.txt")
	for line in fh.readlines():
		print(line,end='')
except: 
	print("Error")
print("After error")

