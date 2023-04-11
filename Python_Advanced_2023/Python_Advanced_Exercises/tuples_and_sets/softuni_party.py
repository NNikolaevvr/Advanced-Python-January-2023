number_of_guests = int(input())
guests = []
vip_and_regular_members = set()
counter = 0
command = input()
while command != 'END':
    guests.append(command)
    command = input()

for i in guests:
    counter = guests.count(i)
    if counter == 1:

        vip_and_regular_members.add(i)

print(len(vip_and_regular_members))

sorted_list = list(sorted(vip_and_regular_members))
print(*sorted_list, sep='\n')