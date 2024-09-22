def SearchB(arr, x):
    indices = []
    for i in range(len(arr)):
        if arr[i] == x:
            indices.append(i)
        elif arr[i] > x:
            
            break
    return indices

arr = sorted([22, 2, 1, 7, 11, 13, 5, 2, 9]) 
x = int(input("Enter the number: "))
result = SearchB(arr, x)
if result:
    print("Output: Index:", result)
else:
    print(f"{x} not found in the array")
