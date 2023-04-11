size_of_matrix = int(input())
matrix = []
row = size_of_matrix
sum_values = 0
found_symbol = False
row_index = 0
column_index = 0
data = []

for i in range(row):
    raw_data = [x for x in input().split()]

    matrix.append(raw_data)


searched_symbol = input()


for i in matrix:
    if data:
        break
    for j in i:
        if searched_symbol in j:
            row_index = matrix.index(i)
            string_element = str(*i)
            column_index = string_element.index(searched_symbol)


            found_symbol = True
            data.append(string_element)
            print(f"({row_index}, {column_index})")
            break


if found_symbol == False:
    print(f"{searched_symbol} does not occur in the matrix")








row = int(input())
matrix = []
even_matrix = []

sum_values = 0
for i in range(row):
    raw_data = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
    matrix.append(raw_data)

print(matrix)
