def Minimum(arr, start, end):
    sub_array = arr[start:end+1]
    
    min_value = min(sub_array)
    
    return arr.index(min_value, start, end+1)

def Sort4(arr):
    for i in range(len(arr)):
        min_index = Minimum(arr, i, len(arr) - 1)
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

X = [-4, 1, 35, 0, -3, 100, 101, 1, 4, -5]

print(Sort4(X))