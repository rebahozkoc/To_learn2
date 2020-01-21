import numpy as np

a = np.array([1,2,3])
print(type(a))
print(a.shape)

b = np.array([[1,2,3, 4, 10],[4,5,6, 7, 8]])
print(b.shape)
print(b)
print(b[1,4])
print("\n\n\n\n")

a = np.zeros((2,3))
print(a)

b = np.ones((1,2))
print(b)
print(type(b[0,0]))

c = np.full((3,7), 144)
print(c)

d = np.eye(4)
print(d)

e= np.random.random((2,2))
print(e)
print("\n\n\n")

######################Slicing######################
a = np.array([[1, 2, 3, 4],[5,6,7,8],[9,10,11,12]])
print(a)
b= a[:2, 1:3]
print(b)
print(a[:, :-1])
print(type(a[1,2]))
print("\n\n\n\n")

#####################Indexing######################
a = np.array([1, 2, 3, 4, 5, 6])
print(a)
print(a[[1,3,5]])

a = np.array([[1, 2], [3, 4], [5, 6]])
print(a)
print()
print(a[[0,1, 2], [0,1,0]])
print(np.array([a[0, 0], a[1, 1], a[2, 0]]))
print("\n\n\n\n")

#################Boolean Indexing##################
print(a)
bool_idx = a > 2
print(bool_idx)

print(a[bool_idx])
print(a[a > 2])
print("\n\n\n\n")

##################Array Math######################
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
# Elementwise sum
print(x + y)
print(np.add(x, y))
# [[ 6 8]
# [10 12]]

# Elementwise product
print(x * y)
print(np.multiply(x, y))
# [[ 5 12]
# [21 32]]

v = np.array([9, 10])
w = np.array([11, 12])

print(v.dot(w))
print(np.dot(v,w))

print(x.dot(v))
print("\n\n\n\n")

##############dot product################

a = np.array([1,2,5])
b  = np.array([3,4,5])
dot = 0
for e, f in zip(a,b):
    print(e,f)
    dot += e*f

print(dot)
print(np.dot(a,b))

print(x.dot(v))
print(x.dot(y))
print("\n\n\n\n")
###############Transposing################3
k = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(k.T)
