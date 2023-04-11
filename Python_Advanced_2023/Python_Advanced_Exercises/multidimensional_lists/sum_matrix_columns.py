size_of_matrix = [int(x) for x in input().split(", ")]
matrix = []
row = int(size_of_matrix[0])
column = int(size_of_matrix[1])
sum_values = 0
for i in range(row):
    raw_data = [int(x) for x in input().split()]

    matrix.append(raw_data)


rows = len(matrix)
cols = len(matrix[0])
sum_of_columns = []

for j in range(cols):
    col_sum = 0
    for k in range(rows):
        col_sum +=matrix[k][j]

    sum_of_columns.append(col_sum)





print(*sum_of_columns, sep="\n")