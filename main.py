def max(list):
    if not list:
        return 'Empty list!'
    max = list[0]
    for num in list:
        if num>max:
            max = num
    return max        
def second_largest(list):
    list.remove(max(list))
    return max(list)

list = [1, 3, 10]    
result = second_largest(list)
print(result)