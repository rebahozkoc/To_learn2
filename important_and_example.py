# An important example for and operator
def r2d2(a):
    b = True
    for k in range(len(a)):
        b = b and bb8(a,k)
    return b

def bb8(a,k):
    print("a", a)
    a[k] = a[k]-1
    return a[k] >= 0

a = [1,2,3,4]
print(r2d2(a))
print(a)
print(r2d2(a))
print(a)
