dic1={'a':'6','b':'2','c':'3'}
ans=dict(sorted(dic1.items(),key=lambda item : item[1]))
print(ans)