row = int(input())
matrix = []
matrix1 = []

sum_values = 0
for i in range(row):
    raw_data = [int(x) for x in input().split(", ")]
    matrix.append(raw_data)


for j in matrix:
    for k in j:
        matrix1.append(k)


print(matrix1)