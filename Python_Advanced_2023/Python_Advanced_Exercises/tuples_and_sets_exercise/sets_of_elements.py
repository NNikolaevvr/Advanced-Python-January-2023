set_numbers = input().split(" ")
first_set = set()
second_set = set()
for i in range(int(set_numbers[0])):
    numbers = input()
    numbers_set1 = first_set.add(int(numbers))

for i in range(int(set_numbers[1])):
    numbers1 = input()
    number_set2 = second_set.add(int(numbers1))

rep_num = first_set.intersection(second_set)

print(*rep_num, sep="\n")
