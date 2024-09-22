from funcs import ShuffleArray
from Insertion import InsertionSort
from MergeSort import MergeSort
import time

# reading the words
def ReadWords():
    wordsFile = open(file='words.txt', mode='r')
    lines = wordsFile.read()
    wordsArray = []
    words = lines.split()
    for word in words:
        wordsArray.append(word)
    return wordsArray

# calculating runtime of sorting functions
def CalculateRuntime(sortingFunction, Array, start, end):
    start_time = time.time()
    sortingFunction(Array, start, end)
    end_time = time.time()
    runtime = end_time - start_time 
    return runtime


wordsArray = ReadWords()
end = len(wordsArray)-1

# insertion sort time before shuffling
arrayCopy = wordsArray.copy()
insertionTime = CalculateRuntime(InsertionSort, arrayCopy, 0, end)
print("The runtime of insertion sort before shuffling: ", insertionTime)

# merge sort time before shuffling
arrayCopy = wordsArray.copy()
mergeSortTime = CalculateRuntime(MergeSort, arrayCopy, 0, end)
print("The runtime of merge sort before shuffling: ", mergeSortTime)

# shuffling the array 
ShuffleArray(wordsArray, 0, end)

# insertion sort runtime after shuffling
arrayCopy = wordsArray.copy()
shuffledInsertionTime = CalculateRuntime(InsertionSort, arrayCopy, 0, end)
print("The runtime of insertion sort after shuffling: ", insertionTime)

# merge sort runtime after shuffling
arrayCopy = wordsArray.copy()
shuffledMergeSortTime = CalculateRuntime(MergeSort, arrayCopy, 0, end)
print("The runtime of merge sort after shuffling: ", mergeSortTime)

# comparison
if shuffledInsertionTime == insertionTime:
    print("They both remain unaffected after shuffling.")
else:
    if shuffledInsertionTime > insertionTime:
        print("Insertion Sort became slower after shuffling.")
    else:
        print("Insertion Sort became faster after shuffling.")


if shuffledMergeSortTime == mergeSortTime:
    print("Merge Sort remain unaffected after shuffling.")
else:
    if shuffledMergeSortTime > mergeSortTime:
        print("Merge Sort became slower after shuffling.")
    else:
        print("Merge Sort became faster after shuffling.")
