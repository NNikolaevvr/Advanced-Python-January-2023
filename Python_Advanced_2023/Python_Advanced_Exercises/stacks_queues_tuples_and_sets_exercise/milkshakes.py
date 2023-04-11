from collections import deque

chocolates = deque(int(x) for x in input().split(", "))
milk = deque(int(x) for x in input().split(", "))

milkshakes = 0

while milkshakes != 5 and chocolates and milk:
    chocolate = chocolates.pop()
    milk_cup = milk.popleft()

    if chocolate <= 0 and milk_cup <= 0:
        continue
    elif chocolate <= 0:
        milk.appendleft(milk_cup)
        continue

    elif milk_cup <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == milk_cup:
        milkshakes +=1

    else:
        milk.append(milk_cup)
        chocolates.append(chocolate - 5)

if milkshakes == 5:
    print(f'Great! You made all the chocolate milkshakes needed!')

else:
    print('Not enough milkshakes.')

print(f"Chocolate: {', '.join(str(x) for x in chocolates) or 'empty' }")
print(f"Milk: {', '.join(str(x) for x in milk) or 'empty' }")