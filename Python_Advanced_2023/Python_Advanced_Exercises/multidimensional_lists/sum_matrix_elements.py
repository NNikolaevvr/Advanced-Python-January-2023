size_of_matrix = [int(x) for x in input().split(", ")]
matrix = []
row = int(size_of_matrix[0])
column = int(size_of_matrix[1])
sum_values = 0
for i in range(row):
    raw_data = [int(x) for x in input().split(", ")]

    matrix.append(raw_data)


for j in range(len(matrix)):
    current_row = matrix[j]

    sum_values += sum(current_row)





print(sum_values)
print(matrix)