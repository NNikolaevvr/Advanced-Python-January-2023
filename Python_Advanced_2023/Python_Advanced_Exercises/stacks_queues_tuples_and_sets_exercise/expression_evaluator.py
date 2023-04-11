from collections import deque
from functools import reduce

expressions = input().split(' ')

i=0

functions= {
    "*": lambda a,b: int(a) * int(b),
    "/": lambda a,b: int(a) / int(b),
    "-": lambda a,b: int(a) - int(b),
    "+": lambda a,b: int(a) + int(b),


}


while i < len(expressions):
    element = expressions[i]

    if not element in functions.keys():
        i+=1
        continue
    result = reduce(functions[element], expressions[:i])

    for i in range(i):
        expressions.pop(1)

    expressions[0] = result

    i=0

print(int(expressions[0]))

