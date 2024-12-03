def flat (nested_list):
    flattened_list=[]
    for item in nested_list :
        if isinstance(item,list):
            flattened_list.extend(flat(item))
        else :
            flattened_list.append(item)
    return flattened_list

l1=[1, [2, [3, 4]], 5]
print(flat(l1))
