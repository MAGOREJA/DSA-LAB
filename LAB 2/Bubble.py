from funcs import RandomArray
import time

def BubbleSort(arr, start, end):
    
    for i in range (start, end):
        for j in range (end-i-1):
            if arr[j] > arr [j+1]:
                arr[j] , arr[j+1] = arr [j+1] , arr[j]

    return arr

start_time = time.time()
sorted_array=BubbleSort(RandomArray(500),11,35)
end_time = time.time()
runtime = end_time - start_time

print("Sorted array:", sorted_array)

print("Runtime of Bubble Sort is" , runtime)

f = open("SortedBubble.csv", mode="w")
for i in sorted_array:
    f.write(str(i) + "\n")