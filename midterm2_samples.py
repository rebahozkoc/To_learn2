def female(n):
    if n == 0:
        return 1
    f = female(n-1)
    return n-male(f)


def male(x):
    if x == 0:
        return 0
    m = male(x-1)
    return x-female(m)

print(male(2))
