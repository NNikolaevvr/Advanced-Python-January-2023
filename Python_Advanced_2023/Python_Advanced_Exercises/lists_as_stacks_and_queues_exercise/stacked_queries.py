integers = int(input())
my_stack = []
new_stack = []
for _ in range(integers):
    commands = input().split(" ")

    if commands[0] == "1":

        my_stack.append(int(commands[1]))

    elif commands[0] == "2":
        if len(my_stack) > 0:
            my_stack.pop()

    elif commands[0] == "3":
        if my_stack:
            print(int(max(my_stack)))

    elif commands[0] == "4":
        if my_stack:

            min_value = min(my_stack)
            print(min_value)


for _ in range(len(my_stack)):
    if len(my_stack) > 0:
        new_stack.append(my_stack.pop())
print(*new_stack, sep = ", ")
