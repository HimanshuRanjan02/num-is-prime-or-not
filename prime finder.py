n=int(input())
fact=0
for i in range(1,n):
    if n%i==0:
        fact+=1
if fact==1:
    print(n,"is prime")
else:
    print(n,"is not prime")