numbers = input().split(" ")
my_stack = []
while len(numbers) > 0:

    my_stack.append(numbers.pop())

print(*my_stack, sep = " ")



