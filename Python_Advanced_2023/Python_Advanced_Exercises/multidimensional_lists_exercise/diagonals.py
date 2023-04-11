size_of_matrix = int(input())
matrix = []
primary_diagonal = []
secondary_diagonal = []

sum_values = 0
sum_secondary = 0
for i in range(size_of_matrix):
    row = input().split(", ")
    raw_data = [int(x) for x in row]

    matrix.append(raw_data)

for j in range(len(matrix)):
    for k in matrix[j]:
        index = matrix.index(matrix[j])
        primary_diagonal.append(matrix[j][index])
        sum_values += matrix[j][index]
        break

for secondary in range(len(matrix)):
    for v in range(len(matrix[secondary]) -1, -1, -1):
        v = abs(secondary - v)
        secondary_diagonal.append(matrix[secondary][v])
        value = matrix[secondary][v]
        sum_secondary += value

        break

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")


