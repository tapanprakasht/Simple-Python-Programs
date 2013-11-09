import sys
import os
def main():
    print('Commamd line arguments are')
    for i in sys.argv:
        print(i)
    print(os.getcwd())

main()

