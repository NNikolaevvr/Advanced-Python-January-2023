from collections import deque

quantity_of_water = int(input())
command = input()


queue = deque()

while command != 'Start':
    queue.append(command)

    command = input()

command = input()
while command != 'End':

    if 'refill' in command:
        command = command.split(" ")
        refill_amount = int(command[1])

        quantity_of_water += refill_amount

    else:
        liters = int(command)
        if liters <= quantity_of_water:
            quantity_of_water -= liters
            print(f"{queue.popleft()} got water")
        else:
            print(f'{queue.popleft()} must wait')
    command = input()
print(f"{quantity_of_water} liters left")

