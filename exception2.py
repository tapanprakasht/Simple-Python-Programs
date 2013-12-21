#!/usr/bin/python3
# Exception Handling -Raise exception

def main():
  try:
    for line in readfile('address.txt'):
      print(line.strip())
  except IOError as e:
    print("Error:",e)
  except ValueError as e:
    print("Error:",e)
    
def readfile(filename):
  if filename.endswith('.txt'):
    fh=open(filename)
    return fh.readlines()
  else:
    raise ValueError('Filename not ends with txt')

if __name__=="__main__":main()