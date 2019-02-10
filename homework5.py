from linear import *
from parse.parse import *

def ltr(colNum, *arg):
    return Matrix([list(arg[i*colNum : (i+1)*colNum])
        for i in range(int(len(arg) / colNum))])

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
print("----- MATRICES -----")
for matrix in matrices:
    print(matrix)
