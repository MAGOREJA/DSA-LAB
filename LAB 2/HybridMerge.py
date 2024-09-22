from funcs import RandomArray
import time

n = 16
def HybridMergeSort(Array, start, end):
    if(end-start + 1) <= n:
        InsertionSort(Array, start, end)
    else:
        mid = (start + end) // 2
        HybridMergeSort(Array, start, mid)
        HybridMergeSort(Array, mid + 1, end)
        Merge(Array, start, mid, end)
    
    return Array
        


def Merge(Array, p, q, r):
    nL = q - p + 1
    nR = r - q

    L = [0] * nL
    R = [0] * nR

    for i in range(nL):
        L[i] = Array[p + i]

    for j in range(nR):
        R[j] = Array[q + 1 + j]

    i = 0  
    j = 0  
    k = p

    while i < nL and j < nR:
        if L[i] <= R[j]:
            Array[k] = L[i]
            i = i + 1
        else:
            Array[k] = R[j]
            j = j + 1
        k = k + 1

    while i < nL:
        Array[k] = L[i]
        i = i + 1
        k = k + 1

    while j < nR:
        Array[k] = R[j]
        j = j + 1
        k = k + 1


def InsertionSort(Array, start, end):
    for j in range(start+1, end):
        key=Array[j]
        i=j-1
        while i>=0 and Array[i]>key:
            Array[i+1]=Array[i]
            i=i-1
        Array[i+1]=key
    return Array


myArray = RandomArray(25) 
lastIndex = len(myArray) - 1

start_time = time.time()
sorted_array=HybridMergeSort(myArray, 0, 15)
end_time = time.time()
runtime = end_time - start_time 

# print("Sorted array:", sorted_array)

print("Runtime for Hybrid Merge Sort is :  ", runtime, "seconds")

f = open("SortedHybridSort.csv", mode="w")
for i in myArray:
    f.write(str(i) + "\n")