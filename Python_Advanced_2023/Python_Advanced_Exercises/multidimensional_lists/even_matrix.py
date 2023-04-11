row = int(input())
matrix = []
even_matrix = []

sum_values = 0
for i in range(row):
    raw_data = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
    matrix.append(raw_data)

print(matrix)
