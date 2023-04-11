def operate(*args):

    if args[0] == '+':
        sum_num = 0
        for i in args[1:]:

            sum_num += i

    elif args[0] == '-':
        sum_num = args[1]
        for i in args[2:]:

            sum_num -= i

    elif args[0] == '*':
        sum_num = 1
        for i in args[1:]:

            sum_num *= i

    elif args[0] == '/':
        sum_num = args[1]
        for i in args[2:]:

            sum_num /= i

    return sum_num



print(operate("/", 3, 4))