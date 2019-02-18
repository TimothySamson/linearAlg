from linear import *
from parse.parse import *

def ltr(colNum, *arg):
    return Matrix([list(arg[i*colNum : (i+1)*colNum])
        for i in range(int(len(arg) / colNum))])

def probno(num):
    print("------- Problem number ", num)

A = Matrix([
    [1, 9, 7],
    [0, 1, -1]
    ])

A = ltr(3, 1, 9, 7, 0, 1, -1)

B = Matrix([
    [1, 7],
    [-1, 9]
    ])

print(-2*B*A)

A = ltr(3, -1, 3, 1, 0, 1, 2)
B = ltr(2, 2, 3, 1, -1)
C = ltr(2, 0, 1, 0, -1)

print(B*(C*A))

B = ltr(2, 1, 2, -1, 3)
C = ltr(2, 0, 1, -1, 0)

print(C * B * C)

htmlstr = open("parse/matrix.html", "r").read()
matrices = html2matrix(htmlstr)

print("---- Problem 16")
A = matrices[33]
B = matrices[34]
C = matrices[35]
print(A * B)
print(A * B * C)
print(B * C)

print("---- Problem 17")
A = matrices[36]
B = matrices[37]
print(A * B)
print(B * A)

probno(18)
A = matrices[38]
B = matrices[39]
C = matrices[40]
print(A * C)
print(B * C)

probno(20)
A = matrices[49]
print(A + A*A)

probno(21)
A = matrices[50]
print(A*A)

probno(24)
A = matrices[53]
B = matrices[54]
print((A * B).transpose())
print(B.transpose() * A.transpose())

probno(25)
A = matrices[55]
print(A.transpose() * A)
print(A * A.transpose())

print("-- Matrices --")
for matrix in matrices:
    print(matrix)
