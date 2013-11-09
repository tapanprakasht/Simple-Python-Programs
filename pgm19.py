def printMax(a,b):
    if a>b:
        print(a," is bigger than ",b)
    else:
        print(b," is bigger than ",a)


def main():
    print("Enter two numbers:")
    a=int(input())
    b=int(input())
    printMax(a,b)

main()

