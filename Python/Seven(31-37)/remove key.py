dic1={'a':'1','b':'2','c':'3'}
key=input()
if key in dic1 :
    remove = dic1.pop(key)
    print(remove)

else :
    print("does not exist")
