number_of_lines = int(input())
converted_name = []
sum_of_name = []
result = []
odd_set = set()
even_set = set()
for i in range(1, number_of_lines + 1):
    name = input()

    for j in name:
        converted_name.append(ord(j))
    sum_of_name.append(sum(converted_name))
    converted_name.clear()
    result.append(sum_of_name.pop() // i)

for i in result:

    if i % 2 == 0:
        even_set.add(i)

    else:
        odd_set.add(i)


if sum(odd_set) == sum(even_set):
    print(*odd_set.union(even_set), sep= ", ")

elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep= ", ")

else:
    print(*odd_set.symmetric_difference(even_set), sep=", ")

