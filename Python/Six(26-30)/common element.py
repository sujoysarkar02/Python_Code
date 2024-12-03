l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
common = list(set(l1) & set(l2))
print(common)