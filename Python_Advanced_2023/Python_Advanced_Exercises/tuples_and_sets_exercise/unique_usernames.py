number_of_names = int(input())
unique_names = set()
for i in range(number_of_names):

    name = unique_names.add(input())

print(*unique_names, sep = "\n")