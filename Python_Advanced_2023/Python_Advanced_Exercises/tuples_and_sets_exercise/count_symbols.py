word = sorted(input())
dict= {}
for i in word:

    dict[i] = word.count(i)


for key, value in dict.items():

    print(f'{key}: {value} time/s', sep="\n")

