def fact(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return res

a=int(input())
if a < 0 :
    print("give positive")
else:
    print(f"factorial of {a} is {fact(a)}")