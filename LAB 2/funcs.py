import random

def RandomArray(size):
    Arr=[]
    for i in range(size-1):
        randomNumber= random.randint(-1000,1000)
        Arr.append(randomNumber)
    return Arr

def ShuffleArray(array, start, end):
    for i in range(end, start-1, -1):
        j = random.randint(0, end)

        array[i], array[j] = array[j], array[i]