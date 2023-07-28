number_of_rows = int(input("Please enter the number of rows in the matrix: "))
number_of_columns = int(input("Please enter the number of columns in the matrix: "))
matrix = []
print("Enter the matrix values: ")
for i in range(0, number_of_rows):
    row = []
    for j in range(0, number_of_columns):
        value = int(input("Value: "))
        row.append(value)
    matrix.append(row)
for row in matrix:
    print("Sum of row: ", sum(matrix[matrix.index(row)]))