def determinant(matrix):
    n = len(matrix)
    
    if n == 1:
        return matrix[0][0]
    
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for j in range(n):
        submatrix = [[matrix[i][k] for k in range(n) if k != j] for i in range(1, n)]
        det += matrix[0][j] * ((-1) ** j) * determinant(submatrix)
    
    return det

def is_singular(matrix):
    det = determinant(matrix)
    return det == 0

def matrix_inverse(matrix):
    if is_singular(matrix):
        return "Matrix is not invertible."

    n = len(matrix)
    identity = [[0] * n for _ in range(n)]
    for i in range(n):
        identity[i][i] = 1

    for i in range(n):
        pivot = matrix[i][i]

        for j in range(n):
            if i != j:
                factor = matrix[j][i] / pivot
                for k in range(n):
                    matrix[j][k] -= factor * matrix[i][k]
                    identity[j][k] -= factor * identity[i][k]

    for i in range(n):
        pivot = matrix[i][i]
        for j in range(n):
            matrix[i][j] /= pivot
            identity[i][j] = round(identity[i][j]/pivot, 6)

    return identity



def solve_linear_equations(A, b):
    inverse_A = matrix_inverse(A)
    if isinstance(inverse_A, str):
        return inverse_A

    x = []
    for i in range(len(A)):
        result = 0
        for j in range(len(A)):
            result += round(inverse_A[i][j] * b[j], 6)
        x.append(result)

    return x

sample_matrices = [
    [[1, 2], 
     [3, 4]],

    [[5, 6], 
     [7, 8]],

    [[1, 2, 3], 
     [4, 5, 6], 
     [7, 8, 9]],

    [[1, 0, 0], 
     [0, 2, 0], 
     [0, 0, 3]],

    [[1, 2, 3], 
     [0, 0, 0], 
     [7, 8, 9]],

    [[1, 2, 3], 
     [3, 6, 9], 
     [2, 4, 6]],

    [[1, 2, 3, 4], 
     [2, 4, 6, 8], 
     [3, 5, 7, 9], 
     [4, 6, 8, 10]],

    [[1, 0, 0, 0], 
     [0, 0, 0, 0], 
     [0, 0, 0, 0], 
     [0, 0, 0, 0]],

    [[1, 1], 
     [1, 1]],

    [[2, 4], 
     [1, 2]],
]

for matrix in sample_matrices:
    print("Input Matrix:")
    for row in matrix:
        print(row)
    
    result = matrix_inverse(matrix)
    if isinstance(result, list):
        print("Inverse Matrix:")
        for row in result:
            print(row)
    else:
        print(result)
    
    print()

A = [[2, 1], [1, 3]]
b = [3, 4]
print("Solving Linear Equation: Ax = b")
print("Coefficient Matrix A:")
for row in A:
    print(row)
print("Right-hand side vector b:", b)
solution = solve_linear_equations(A, b)
if isinstance(solution, list):
    print("Solution vector x:", solution)
else:
    print(solution)
