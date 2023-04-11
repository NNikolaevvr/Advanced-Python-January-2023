list_of_coffee = input().split()
lines = int(input())

for i in range(lines):
    commands = input().split()

    if commands[0] == "Include":
        list_of_coffee.append(commands[1])

    elif commands[0] == "Remove":
        if int(commands[2]) < len(list_of_coffee):
            if commands[1] == "first":
                list_of_coffee = list_of_coffee[int(commands[2]):]
            elif commands[1] == "last":
                list_of_coffee = list_of_coffee[:-int(commands[2])]

        # if commands[1] == "first":
        #     list_of_coffee.pop(0)
        # elif commands[1] == "last":
        #     list_of_coffee.pop()

    elif commands[0] == "Prefer":
        index_one = int(commands[1])
        index_two = int(commands[2])

        if index_one < len(list_of_coffee) and index_two < len(list_of_coffee):
            list_of_coffee[index_one], list_of_coffee[index_two] = list_of_coffee[index_two], list_of_coffee[index_one]

    elif commands[0] == "Reverse":
        list_of_coffee.reverse()

print("Coffees:")
print(" ".join(list_of_coffee))