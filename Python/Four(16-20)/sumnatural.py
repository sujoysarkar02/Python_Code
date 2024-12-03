def sum(start,n):
    s=0
    for i in range(start,n+1):
        s+=i
    return s


start=int(input())
n=int(input())
if start > 0 and start <=n :
    total = sum(start,n)
    print(total)
else:
    print("try again")