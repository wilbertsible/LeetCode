import copy
a = [1,2,[3,4],5]
b = copy.deepcopy(a)
b[2][1] = 10

print(a)
print(b)