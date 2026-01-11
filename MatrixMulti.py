# Matrix Multiplication in Python (without libraries)

# Input matrix dimensions
r1 = int(input("Enter number of rows of first matrix: "))
c1 = int(input("Enter number of columns of first matrix: "))

r2 = int(input("Enter number of rows of second matrix: "))
c2 = int(input("Enter number of columns of second matrix: "))

# Check multiplication condition
if c1 != r2:
    print("Matrix multiplication not possible")
else:
    # Input first matrix
    print("Enter elements of first matrix:")
    A = [[int(input()) for j in range(c1)] for i in range(r1)]

    # Input second matrix

    print("Enter elements of second matrix:")
    B = [[int(input()) for j in range(c2)] for i in range(r2)]

    # Result matrix
    C = [[0 for j in range(c2)] for i in range(r1)]

    # Matrix multiplication logic
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                C[i][j] += A[i][k] * B[k][j]

    # Display result
    print("Resultant Matrix:")
    for row in C:
        print(row)   