from funcs import RandomArray
import time

def MergeSort(Array, p, r):
    if p < r:
        q = (p + r) // 2

        MergeSort(Array, p, q)
        MergeSort(Array, q + 1, r)

        Merge(Array, p, q, r)
    
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


start_time = time.time()
sorted_array=MergeSort(RandomArray(300),10,25)
end_time = time.time()
runtime = end_time - start_time

print("Sorted array:", sorted_array)

print("Runtime of Merge Sort is" , runtime)

f = open("SortedMerge.csv", mode="w")
for i in sorted_array:
    f.write(str(i) + "\n")