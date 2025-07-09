#initializing matrixa, matrixb multiplying 1st row with 1st coloumn 
a = int(input("Enter number of rows for matrix A: "))
b = int(input("Enter number of columns for matrix A: "))
c = int(input("Enter number of rows for matrix B: "))
d = int(input("Enter number of columns for matrix B: "))
if b != c:
    print("Error: Matrices cannot be multiplied!")
else:
    matrixa = [[0 for _ in range(b)] for _ in range(a)]
    matrixb = [[0 for _ in range(d)] for _ in range(c)]
    
    print("Enter elements for Matrix A:")
    for i in range(a):
        for j in range(b):
            matrixa[i][j] = int(input(f"Enter element at ({i+1},{j+1}): "))

    print("Enter elements for Matrix B:")
    for i in range(c):
        for j in range(d):
            matrixb[i][j] = int(input(f"Enter element at ({i+1},{j+1}): "))

    result = [[0 for _ in range(d)] for _ in range(a)]
    for i in range(a):
        for j in range(d):
            for k in range(b):
                result[i][j] += matrixa[i][k] * matrixb[k][j]

    print("Result of Matrix Multiplication:")
    print(result)