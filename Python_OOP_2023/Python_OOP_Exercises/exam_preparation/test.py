from functools import reduce

a = ['1','2','3']

x = list(map(int, a ))




a = reduce(lambda x,y: x*y, x)

print(a)