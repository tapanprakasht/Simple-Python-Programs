sum=0;
n=int(input("Enter the limit:"))
for i in range(1,n,1):
    if i%3==0 or i%5==0:
        sum=sum+i
print("Sum=%d" %(sum))
