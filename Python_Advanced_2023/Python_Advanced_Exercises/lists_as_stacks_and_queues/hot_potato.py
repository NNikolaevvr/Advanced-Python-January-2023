from collections import deque

name_of_players = input().split(" ")
step_of_hot_potato = int(input())
players_queue = deque(name_of_players)
counter = 0

while len(players_queue) > 1:
    counter +=1
    current_name_of_player = players_queue.popleft()
    if counter == step_of_hot_potato:
        print(f'Removed {current_name_of_player}')
        counter = 0

    else:
        players_queue.append(current_name_of_player)

print(f'Last is {players_queue[0]}')