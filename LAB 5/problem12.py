numbers = [10, -17, 9, 1, -2, 18, -11, 0]

# (a) Remove all negative numbers
positive_numbers = [num for num in numbers if num >= 0]

# (b) Find the maximum and minimum values
max_value = max(positive_numbers) if positive_numbers else None
min_value = min(positive_numbers) if positive_numbers else None

# (c) Compute the average of the elements
average = sum(positive_numbers) / len(positive_numbers) if positive_numbers else 0

print("Positive numbers:", positive_numbers)
print("Maximum value:", max_value)
print("Minimum value:", min_value)
print("Average:", average)
