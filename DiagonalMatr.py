# Input size of square matrix
n = int(input("Enter size of square matrix (n x n): "))

matrix = []

# Input matrix
print("Enter matrix elements row-wise:")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

left_diag_sum = 0
right_diag_sum = 0

# Diagonal sums
for i in range(n):
    left_diag_sum += matrix[i][i]           # Left diagonal
    right_diag_sum += matrix[i][n - i - 1]  # Right diagonal

# Middle column sum (only if n is odd)
mid_col_sum = 0
if n % 2 == 1:
    mid = n // 2
    for i in range(n):
        mid_col_sum += matrix[i][mid]

# Output
print("Left diagonal sum =", left_diag_sum)
print("Right diagonal sum =", right_diag_sum)

if n % 2 == 1:
    print("Middle column sum =", mid_col_sum)
else:
    print("No middle column (matrix size is even)")