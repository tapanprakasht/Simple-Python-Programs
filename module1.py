#!/usr/bin/python3
import sys
def main():
  print("Python version {}.{}.{}".format(*sys.version_info))
  print(sys.platform)
if __name__=="__main__":main()