def most_freq(lst):
    if not lst :
        return "None"
    frequency = {}
    for element in lst :
        if element in frequency :
            frequency[element]+=1
        else :
            frequency[element]=1

    most_freq=max(frequency,key=frequency.get)
    return most_freq

my_list = list(map(int,input().split()))
result = most_freq(my_list)
print(result)

