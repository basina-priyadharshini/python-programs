# Input matrix size
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

# Input matrix
print("Enter matrix elements row-wise:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Find row sums and maximum
max_sum = None
max_row = 0

for i in range(rows):
    row_sum = sum(matrix[i])
    print(f"Sum of row {i+1} = {row_sum}")

    if max_sum is None or row_sum > max_sum:
        max_sum = row_sum
        max_row = i + 1

# Output result
print("\nRow with maximum sum:")
print(f"Row number: {max_row}")
print(f"Maximum sum: {max_sum}")