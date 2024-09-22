from funcs import RandomArray
import time

def InsertionSort(array, start, end):
    for j in range(start+1, end):
        key=array[j]
        i=j-1
        while i>=0 and array[i]>key:
            array[i+1]=array[i]
            i=i-1
        array[i+1]=key
    return array

start_time = time.time()
sorted_array=InsertionSort(RandomArray(500),11,35)
end_time = time.time()
runtime = end_time - start_time

# print(sorted_array)

print("Runtime of Insertion Sort is " , runtime, "seconds.")

f = open("SortedInsertion.csv", mode="w")
for i in sorted_array:
    f.write(str(i) + "\n")