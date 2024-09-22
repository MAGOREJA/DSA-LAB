def RowWiseSum(Mat):
    return [sum(row) for row in Mat]

def ColumnWiseSum(Mat):
    num_cols = len(Mat[0])
    column_sums = [0] * num_cols
    
    for row in Mat:
        for i in range(num_cols):
            column_sums[i] += row[i]
    
    return column_sums

A = [
    [1, 13, 13],
    [5, 11, 6],
    [4, 4, 9]
]

row_wise_sum = RowWiseSum(A)
column_wise_sum = ColumnWiseSum(A)

print(f"Row-wise sum: {row_wise_sum}")
print(f"Column-wise sum: {column_wise_sum}")