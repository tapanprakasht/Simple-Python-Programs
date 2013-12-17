#!/usr/bin/python3
fh=open("address.txt")
for line in fh.readlines():
    print(line,end='')
print("Reading finished")

