def find(numbers):
    unique_num = list(set(numbers))
    if len(unique_num) < 2:
        return "NO number"
    unique_num.sort(reverse = True)
    return unique_num[1]

num_list =list(map(int,input().split()))
sec=find(num_list)
print(sec)