def gen(l1):
    for i in l1:
        yield i**2
x = gen([2,4,6,8])
for i in x:
    print(i)
