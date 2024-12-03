def remove (l1) :
    return list(set(l1))
    

l1=list(map(int,input().split()))
result = remove(l1)
print(result)