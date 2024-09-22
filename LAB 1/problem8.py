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