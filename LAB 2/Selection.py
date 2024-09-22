from funcs import RandomArray
import time

def SelectionSort(arr, start, end):
  
    for i in range (start, end):
        min = i
        for j in range (i+1,end):
            if arr[j]< arr[min]:
                min = j
            arr[i], arr[min] = arr[min],arr[i]
    return arr


start_time = time.time()
sorted_array=SelectionSort(RandomArray(500),11,35)
end_time = time.time()
runtime = end_time - start_time

print("Sorted array:", sorted_array)

print("Runtime of Selection Sort is" , runtime)

f = open("SortedSelection.csv", mode="w")
for i in sorted_array:
    f.write(str(i) + "\n")