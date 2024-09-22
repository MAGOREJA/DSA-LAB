def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Recursive calls to sort both halves
        merge_sort(left_half)
        merge_sort(right_half)
        
        i = j = 0
        merged = []  # New list to store merged result
        
        # Merging the two halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                merged.append(left_half[i])
                i += 1
            else:
                merged.append(right_half[j])
                j += 1
        
        # Append any remaining elements from left_half
        while i < len(left_half):
            merged.append(left_half[i])
            i += 1
        
        # Append any remaining elements from right_half
        while j < len(right_half):
            merged.append(right_half[j])
            j += 1
        
        # Copy the merged result back into the original array
        arr[:] = merged

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("Sorted array:", arr)
