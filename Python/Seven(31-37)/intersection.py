def find(set1,set2):
    inter = set1.intersection(set2)
    return inter
set1=input()
set2=input()
set1=set(map(int,set1.split()))
set2=set(map(int,set2.split()))
result = find(set1,set2)
print(result)