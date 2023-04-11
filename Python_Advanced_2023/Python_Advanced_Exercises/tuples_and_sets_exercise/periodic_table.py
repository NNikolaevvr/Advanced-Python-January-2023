number_of_lines = int(input())
unique = []
list_unique = []
for i in range(number_of_lines):
    chemicals = input().split(" ")

    while chemicals:


        list_unique.append(chemicals.pop())


list_unique = set(list_unique)


print(*list_unique, sep= "\n")

