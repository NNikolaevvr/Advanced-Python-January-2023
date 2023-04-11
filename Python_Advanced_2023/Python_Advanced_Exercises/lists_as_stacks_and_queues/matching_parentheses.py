word = input()
parentheses = []

for i in range(len(word)):
    if word[i] == '(':
        parentheses.append(i)

    elif word[i] == ')':
        start_index = parentheses.pop()
        print(word[start_index:i + 1])