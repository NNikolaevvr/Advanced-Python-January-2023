from collections import deque

rows, cols = [int(x) for x in input().split()]
snake = input()

index_snake = 0

for row in range(rows):
    result = deque()
    for col in range(cols):
        if index_snake == len(snake):
            index_snake = 0
        if row % 2 == 0:
            result.append(snake[index_snake])
        else:
            result.appendleft(snake[index_snake])
        index_snake += 1
    print("".join(result))