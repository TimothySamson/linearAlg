from linear import *

print("----------")

A = Matrix([
    [1, -4],
    [6, 5],
    [-2, 3]
])

B = Matrix([
    [1, 4],
    [-1, 5],
    [1, 10]
])

print(A+B)
print(A-B)
print(2*A)
print(2*A - B)
print(B + 0.5*A)

print("----------")

A = Matrix([
    [4, 3, 3],
    [-5, 1, 2]
])

B = Matrix([
    [1, 2, -7],
    [0, -5, 1]
])
print((2*A - 3*B)[0][2])
print((2*A - 3*B)[1][1])

print("----------")

A = Matrix([
    [1, 2],
    [4, 2]
    ])
B = Matrix([
    [2, -1],
    [-1, 8]
    ])

print(A*B)
print(B*A)

print("----------")

A = Matrix([
    [-1, 2, 3],
    [2, 2, 3,],
    [5, 1, -2]
    ])
B = Matrix([
    [0, 1, 2],
    [1, -4, -4],
    [-1, -2, 3]
    ])

print(A*B)
print(B*A)

print("----------")

A = Matrix([
    [3, 1],
    [-3, 4],
    [1, 5]
    ])

B = Matrix([
    [0, -1, 0],
    [3, 0, 1],
    [8, -1, 6]
    ])

# print(A*B)
print(B*A)

print("----------")

A = Matrix([[1, 2, -1, -2]]).transpose()
B = Matrix([
    [2, 1, 2, 3]
    ])

print(A*B)
print(B*A)

print("----------")

A = Matrix([
    [5, -1, -1],
    [1, -5, 6]
    ])

print(A.rref().fracStr())

print("-----------")

A = Matrix([
    [-1, 1, 8],
    [-2, 1, 0]
    ])

print(A.rref())

print("------------")
A = Matrix([
    [1, -2, 3, 27],
    [-1, 3, -1, -12],
    [2, -5, 5, 47]
    ])
print(A.rref())

print("------------")

print(Matrix([
    [-1, -3, 1, -5],
    [3, 2, 1, 7]
    ]).rref().fracStr())

print("------------")

print(Matrix([
    [1, 1, -2, 10],
    [1, 0, -1, 1],
    [9, -1, -1, 0]
    ]).rref())
