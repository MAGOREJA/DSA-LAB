def Minimum(arr, start, end):
    sub_array = arr[start:end+1]
    
    min_value = min(sub_array)
    
    return arr.index(min_value, start, end+1)

arr = [3, 4, 7, 8, 0, 1, 23, -2, -5]
start = 4
end = 7

print(Minimum(arr, start, end))