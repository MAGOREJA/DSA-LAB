students = ["Alice", "Bob", "Charlie", "David", "Eva"]
search_name = input("Enter the name to search for: ")

if search_name in students:
    index = students.index(search_name)
    print(f"{search_name} found at index {index}.")
else:
    print(f"{search_name} is not present in the list.")
