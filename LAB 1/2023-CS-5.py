# problem 1
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

# problem 2
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

# problem 3
def Minimum(arr, start, end):
    sub_array = arr[start:end+1]
    
    min_value = min(sub_array)
    
    return arr.index(min_value, start, end+1)

arr = [3, 4, 7, 8, 0, 1, 23, -2, -5]
start = 4
end = 7

print(Minimum(arr, start, end))

# problem 4
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

# problem 5
def StringReverse(str, start, end):
    sub_string = str[start:end+1]
    
    if len(sub_string) == 0:
        return sub_string
    else:
        return sub_string[-1] + StringReverse(sub_string[:-1], 0, len(sub_string) - 2)

str = "University of Engineering and Technology Lahore"
start = 20  
end = 40    

print(StringReverse(str, start, end))

# problem 6
def SumIterative(number):
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

def SumRecursive(number):
    if number == 0:
        return 0
    else:
        return number % 10 + SumRecursive(number // 10)

number = int(input("Give Number: "))

sum_iterative = SumIterative(number)
sum_recursive = SumRecursive(number)

print(f"Sum using iterative method: {sum_iterative}")
print(f"Sum using recursive method: {sum_recursive}")

# problem 7
def RowWiseSum(Mat):
    return [sum(row) for row in Mat]

def ColumnWiseSum(Mat):
    num_cols = len(Mat[0])
    column_sums = [0] * num_cols
    
    for row in Mat:
        for i in range(num_cols):
            column_sums[i] += row[i]
    
    return column_sums

A = [
    [1, 13, 13],
    [5, 11, 6],
    [4, 4, 9]
]

row_wise_sum = RowWiseSum(A)
column_wise_sum = ColumnWiseSum(A)

print(f"Row-wise sum: {row_wise_sum}")
print(f"Column-wise sum: {column_wise_sum}")

# problem 8
def SortedMerge(Arr1, Arr2):

  merged_array = []
  i = 0
  j = 0
  while i < len(Arr1) and j < len(Arr2):
    if Arr1[i] <= Arr2[j]:
      merged_array.append(Arr1[i])
      i += 1
    else:
      merged_array.append(Arr2[j])
      j += 1

  while i < len(Arr1):
    merged_array.append(Arr1[i])
    i += 1
  while j < len(Arr2):
    merged_array.append(Arr2[j])
    j += 1

  return merged_array

A = [0, 3, 4, 10, 11]
B = [1, 8, 13, 24]

merged_array = SortedMerge(A, B)
print(merged_array)

# problem 9
def PalindromRecursive(str):
    if len(str) <= 1:
        return True
    elif str[0] == str[-1]:
        return PalindromRecursive(str[1:-1])
    else:
        return False
    
print(PalindromRecursive("radar"))

# problem 10
def Sort10(arr):
    arr.sort()

    result = []
    
    negatives = [x for x in arr if x < 0]
    result.extend(negatives)
    
    non_neg_odds = [x for x in arr if x >= 0 and x % 2 != 0]
    if non_neg_odds:
        result.append(non_neg_odds[0])
    
    remaining_negatives = [x for x in arr if x < 0 and x not in result]
    result.extend(remaining_negatives)

    remaining_odds = [x for x in arr if x >= 0 and x % 2 != 0 and x not in result]
    result.extend(remaining_odds)

    non_negatives = [x for x in arr if x >= 0 and x not in result]
    result.extend(non_negatives)
    
    return result

arr = [10, -1, 9, 20, -3, -8, 22, 9, 7]
sorted_arr = Sort10(arr)
print(sorted_arr)