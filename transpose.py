#initializing matrix and empty matrix(transpose) and simply printing the initialized matrix position oppositely (a,b)th element in matrix is equal to (b,a)th element in transpose 
a = int(input("Enter number of rows for matrix: "))
b = int(input("Enter number of columns for matrix: "))
matrix_exp = [[0 for _ in range(b)] for _ in range(a)]

print("Enter elements for Matrix:")
for i in range(a):
    for j in range(b):
        matrix_exp[i][j] = int(input(f"Enter element at ({i+1},{j+1}): "))

transpose = [[0 for _ in range(a)] for _ in range(b)]
for i in range(a):
    for j in range(b):
        transpose[j][i] = matrix_exp[i][j]
print(transpose)
