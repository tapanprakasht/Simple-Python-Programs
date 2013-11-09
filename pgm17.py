n=int(input("Enter a number:"))
k=n
for i in range(1,n+1,1):
    for m in range(1,k,1):
        print('  ',end='')
    k=k-1
    for j in range(1,i+1,1):
        print(j,' ',end='')
    print('\n')

