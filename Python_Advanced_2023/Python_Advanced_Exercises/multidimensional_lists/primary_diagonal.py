size_of_matrix = int(input())
matrix = []
row = size_of_matrix
sum_values = 0

for i in range(row):
    raw_data = [int(x) for x in input().split()]

    matrix.append(raw_data)

for j in range(len(matrix)):
    for k in matrix[j] :
        index = matrix.index(matrix[j])
        sum_values += matrix[j][index]
        break




print(sum_values)