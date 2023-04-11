number_of_lines = int(input())

max_intersection = 0
longest_intersection = set()
first_set = set()
second_set = set()

for i in range(number_of_lines):
    intersections = input().split("-")

    first = intersections[0].split(",")
    second = intersections[1].split(",")
    for i in range(len(first)):

        first[i] = int(first[i])

    for i in range(len(second)):

        second[i] = int(second[i])

    for number in range(first[0], first[1] + 1):
        first_set.add(number)

    for number in range(second[0], second[1] + 1):
        second_set.add(number)


    sets_intersection = first_set.intersection(second_set)

    if len(sets_intersection) > max_intersection:
        max_intersection = len(sets_intersection)

        longest_intersection = sets_intersection

    first_set.clear()
    second_set.clear()

print(f"Longest intersection is {[num for num in longest_intersection]} with length {max_intersection}")