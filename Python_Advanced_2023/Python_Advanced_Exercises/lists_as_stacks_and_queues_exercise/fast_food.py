from collections import deque

quantity_of_the_food = int(input())

quantity_of_food_order = deque([int(x) for x in input().split(" ")])

print(int(max(quantity_of_food_order)))


for order in quantity_of_food_order.copy():
    if quantity_of_the_food >= order:
        quantity_of_the_food -= order
        quantity_of_food_order.popleft()
    else:
        break

if not quantity_of_food_order:
    print("Orders complete")

else:
    print(f"Orders left: {' '.join([str(x) for x in quantity_of_food_order])}")




