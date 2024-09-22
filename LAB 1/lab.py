# task 1
print ("Hello to Data Structure and Algorithms Course")
# task 2
a = 69
print("The value of a is: ", a)

# task 3
a = input("Enter the value: ") 
b = int(a)
print("Entered value is: " + str(b))

# task 4
array = []
array = [1,2,6,10,4]
arr = [[1,3,2], [1,5,6]]

# task 5
array = 0 * 10 
array1 = [[0 for x in range(4)] for y in range(3)]

#task 6
def sum(n):
    if n == 0:
        return n 
    else: 
        return n + sum(n-1)
print (sum (10))

#task 7
def printArray (arr, start, end):
    if start == end:
        print(arr[start])
    else:
        print(arr[start])
        printArray (arr, start+1, end)
arr = [1,2,3,4,5,6,7,8,9,10]
printArray (arr, 0, len(arr)-1)

#task 8
def power (n, k):
    if k == 1:
        return n
    else:
        return n * power (n, k-1)

# numpy
import numpy as np

arr = np.zeros(10)
for n in range(len(arr)):
    print(arr[n])

# idk
