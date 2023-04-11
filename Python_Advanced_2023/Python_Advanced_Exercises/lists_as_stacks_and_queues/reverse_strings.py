reverse_word = list(input())
stack = []

for i in range(len(reverse_word)):
    stack.append(reverse_word.pop())


print(*stack, sep="")

