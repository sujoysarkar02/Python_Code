def check(n):
    if n%2 == 0 :
        return "Is an even"
    else :
        return "Is an odd"
    
a=int(input())
result = check(a)
print(result)