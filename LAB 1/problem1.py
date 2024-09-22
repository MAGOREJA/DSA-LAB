def SearchA(arr, x):
    index = []
    for i in range(len(arr)):
        if arr[i] == x:
            index.append(i)
    return index

arr = [22, 2, 1, 7, 11, 13, 5, 2, 9]
x = int(input("Enter the number: "))
result = SearchA(arr, x)
if result:
    print("Index:", result)
else:
    print(str(x) + " not found in the array")