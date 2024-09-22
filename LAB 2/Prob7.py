from funcs import RandomArray
from Bubble import BubbleSort
from Insertion import InsertionSort
from MergeSort import MergeSort
from HybridMerge import HybridMergeSort
from Selection import SelectionSort
import csv
import time

def ReadNvalues():
    numbersFile = open(file='Nvalues.txt', mode='r')
    lines = numbersFile.read()
    arraySizes = []
    numbers = lines.split()
    for n in numbers:
        num = int(n)
        arraySizes.append(num)
    return arraySizes

def CalculateRuntime(sortFunction, myArray, start, end):
    start_time = time.time()
    sortFunction(myArray, start, end)
    end_time = time.time()
    runtime = end_time - start_time 
    return runtime

f = open("Runtime.csv", mode="w")
writer = csv.writer(f)
# writing the header of the file 
writer.writerow(["Value of n", "Insertion sort (seconds)", "Merge sort (seconds)", "Hybrid Merge sort (seconds)", "Selection sort (seconds)", "Bubble sort (seconds)"])

arraySizes = ReadNvalues()
for n in arraySizes:
    randArray = RandomArray(n)
    lastIndex = len(randArray) - 1

    # Insertion sort time
    arrayCopy = randArray.copy()
    insertionTime = CalculateRuntime(InsertionSort, arrayCopy, 0, lastIndex)

    # Merge sort time
    arrayCopy = randArray.copy()
    mergeSortTime = CalculateRuntime(MergeSort, arrayCopy, 0, lastIndex)

    # Hybrid Merge sort time
    arrayCopy = randArray.copy()
    hybridTime = CalculateRuntime(HybridMergeSort, arrayCopy, 0, lastIndex)

    # Selection sort time
    arrayCopy = randArray.copy()
    selectionTime = CalculateRuntime(SelectionSort, arrayCopy, 0, lastIndex)

    # Bubble sort time
    arrayCopy = randArray.copy()
    bubbleTime = CalculateRuntime(BubbleSort, arrayCopy, 0, lastIndex)

   # writing the lines in runtime csv file
    writer.writerow([n, insertionTime, mergeSortTime, hybridTime, selectionTime, bubbleTime])
