from functools import reduce

li = [1,2,3,4]
num = reduce(lambda x,y : (x+y), li)
print(num)