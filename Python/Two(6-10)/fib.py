def fib(n):
    a=0
    b=1
    for _ in range(n):
        print(a,end=" ")
        next=a+b
        a=b
        b=next

n=int(input())
if n <= 0:
    print("enter positive")

else :
    print("the fibonacci series of {a} is")
    fib(n)