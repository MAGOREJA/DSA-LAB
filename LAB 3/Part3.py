def printMatrix(A, starting_index, rows, columns):
    x, y = starting_index
    for i in range(rows):
        for j in range(columns):
            print(A[x + i][y + j], end=' ')
        print()

matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]
printMatrix(matrix, (1, 2), 2, 3) 
def MatAdd(A, B):
    rows = len(A)
    cols = len(A[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            result[i][j] = A[i][j] + B[i][j]
    
    return result

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(MatAdd(A, B))  
def MatAddPartial(A, B, start, size):
    x, y = start
    result = [[0 for _ in range(size)] for _ in range(size)]
    
    for i in range(size):
        for j in range(size):
            result[i][j] = A[x + i][y + j] + B[x + i][y + j]
    
    return result

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
print(MatAddPartial(A, B, (1, 1), 2))  
def MatMul(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    
    if cols_A != rows_B:
        raise ValueError("Number of A columns must equal number of B rows")
    
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(MatMul(A, B))  
def MatMulRecursive(A, B, i, j, k):
    if k == 0:
        return 0
    return A[i][k - 1] * B[k - 1][j] + MatMulRecursive(A, B, i, j, k - 1)

def MatMulRec(A, B):
    rows_A = len(A)
    cols_B = len(B[0])
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    for i in range(rows_A):
        for j in range(cols_B):
            result[i][j] = MatMulRecursive(A, B, i, j, len(B))
    
    return result

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(MatMulRec(A, B)) 
def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def subtract(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def MatMulStrassen(A, B):
    n = len(A)
    
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    
    mid = n // 2
    
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]
    
    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]
    
    M1 = MatMulStrassen(add(A11, A22), add(B11, B22))
    M2 = MatMulStrassen(add(A21, A22), B11)
    M3 = MatMulStrassen(A11, subtract(B12, B22))
    M4 = MatMulStrassen(A22, subtract(B21, B11))
    M5 = MatMulStrassen(add(A11, A12), B22)
    M6 = MatMulStrassen(subtract(A21, A11), add(B11, B12))
    M7 = MatMulStrassen(subtract(A12, A22), add(B21, B22))

    C11 = add(subtract(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(subtract(add(M1, M3), M2), M6)

    C = []
    for i in range(mid):
        C.append(C11[i] + C12[i])
    for i in range(mid):
        C.append(C21[i] + C22[i])

    return C

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(MatMulStrassen(A, B)) 
def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def subtract(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def MatMulStrassen(A, B):
    n = len(A)
    
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    
    mid = n // 2
    
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]
    
    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]
    
    M1 = MatMulStrassen(add(A11, A22), add(B11, B22))
    M2 = MatMulStrassen(add(A21, A22), B11)
    M3 = MatMulStrassen(A11, subtract(B12, B22))
    M4 = MatMulStrassen(A22, subtract(B21, B11))
    M5 = MatMulStrassen(add(A11, A12), B22)
    M6 = MatMulStrassen(subtract(A21, A11), add(B11, B12))
    M7 = MatMulStrassen(subtract(A12, A22), add(B21, B22))

    C11 = add(subtract(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(subtract(add(M1, M3), M2), M6)

    C = []
    for i in range(mid):
        C.append(C11[i] + C12[i])
    for i in range(mid):
        C.append(C21[i] + C22[i])

    return C

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(MatMulStrassen(A, B))  
