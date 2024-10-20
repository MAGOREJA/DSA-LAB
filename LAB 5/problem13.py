grid = []

def add_row(row):
    grid.append(row)

def add_column(column):
    for i in range(len(grid)):
        grid[i].append(column[i] if i < len(column) else 0)

def display_grid():
    for row in grid:
        print(row)

def sum_elements():
    total = 0
    for row in grid:
        total += sum(row)
    return total

add_row([1, 2, 3])
add_row([4, 5, 6])
add_row([7, 8, 9])
print("Initial grid:")
display_grid()

add_column([10, 11, 12])
print("\nGrid after adding a column:")
display_grid()

total_sum = sum_elements()
print("\nSum of all elements in the grid:", total_sum)
