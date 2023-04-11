first_numbers = set(int(x) for x in input().split(" "))
second_numbers = set(int(y) for y in input().split(" "))

number_of_lines = int(input())

for i in range(number_of_lines):
    command = input().split(" ")
    operation = command[0], command[1]
    operation = " ".join(operation)

    if operation == "Add First":

        digit = [x for x in command if x.isdigit()]
        for i in digit:
            first_numbers.add(int(i))
    elif operation == "Add Second":
        digit = [x for x in command if x.isdigit()]
        for i in digit:
            second_numbers.add(int(i))

    elif operation == "Remove First":

        digit = [int(x) for x in command if x.isdigit()]


        for i in digit:
            first_numbers.discard(int(i))


    elif operation == "Remove Second":

        digit = [int(x) for x in command if x.isdigit()]
        for j in digit:

            second_numbers.discard(int(j))

    elif operation == "Check Subset":
        if second_numbers.issubset(first_numbers):
            print("True")
        elif first_numbers.issubset(second_numbers):
            print("True")


        else:
            print("False")

print(*sorted(first_numbers), sep= ", ")
print(*sorted(second_numbers), sep= ", ")
