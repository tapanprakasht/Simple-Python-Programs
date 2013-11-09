def myFunction(num):
  if num<1:
    raise "Error1",num

def main():
  n=int(input("Enter a number:"))
  try:
    myFunction(n)
  except "Error1",num:
    print "Invalid number"

main()
