import time

student_list = []
time_records = []

for num in range(1, 101):
    start = time.time()
    student_list.append(num)
    end = time.time()
    
    elapsed_time = end - start
    time_records.append(elapsed_time)

print("Time taken for each append operation:")
for index, elapsed_time in enumerate(time_records):
    print(f"Appending {index + 1}: {elapsed_time:.10f} seconds")

print("\nDid the time increase as the list grows?")
for i in range(1, len(time_records)):
    if time_records[i] > time_records[i - 1]:
        print(f"At index {i + 1}, time increased: {time_records[i]:.10f} seconds (previous: {time_records[i - 1]:.10f} seconds)")
