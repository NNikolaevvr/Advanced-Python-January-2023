number_of_names = int(input())
unique_names = set()
for i in range(number_of_names):
    names = input()
    unique_names.add(names)


print(*unique_names, sep="\n")