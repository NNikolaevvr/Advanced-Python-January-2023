from collections import deque

size_of_eggs = list(map(int, input().split(", ")))
size_of_pieces_of_paper = list(map(int, input().split(", ")))

size_of_box = 50
filled_box = 0

size_of_eggs = deque(size_of_eggs)
size_of_pieces_of_paper = deque(size_of_pieces_of_paper)
while size_of_eggs and size_of_pieces_of_paper:
    egg = size_of_eggs.popleft()
    paper = size_of_pieces_of_paper.pop()

    if egg <= 0:
        size_of_pieces_of_paper.append(paper)
        continue

    if egg == 13:
        first_paper = size_of_pieces_of_paper.popleft()
        size_of_pieces_of_paper.append(first_paper)
        size_of_pieces_of_paper.appendleft(paper)
        continue


    wrapped_egg = egg + paper

    if wrapped_egg <= 50:
        filled_box+= 1




if filled_box > 0:
    print(f'Great! You filled {filled_box} boxes.')

else:
    print("Sorry! You couldn't fill any boxes!")

if size_of_eggs:
    print(f"Eggs left: {', '.join(str(x) for x in size_of_eggs)}")

elif size_of_pieces_of_paper:
    print(f"Pieces of paper left: {', '.join(str(x) for x in size_of_pieces_of_paper)}")