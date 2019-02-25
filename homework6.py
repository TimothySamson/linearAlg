from parse.parse import *
from linear import *

def ltr(colNum, *arg):
    return Matrix([list(arg[i*colNum : (i+1)*colNum])
        for i in range(int(len(arg) / colNum))])

def probno(num):
    print("------- Problem number ", num)

htmlstr = open("parse/matrix.html", "r").read()
matrices = html2matrix(htmlstr)


probno(1)
A = matrices[0]
B = matrices[1]

print(A * B)

probno(2)
A = matrices[2]
B = matrices[3] / 3

print(A*B)
print(B*A)

probno(3)

A = matrices[4]
print(A**-1)

probno(4)
M = matrices
A = M[5]

print(A**-1)

probno(5)
A = M[6]
print(A.inverse())

print("Problem 6 - 10")
for i in range(7, 11):
    try:
        print((M[i]**-1).fracStr())
    except:
        print("DNE")

probno(10)
A = M[11]

print(A.inverse()**-2)
print((A.inverse()**2).fracStr())
print((A**2).inverse().fracStr())

probno(11)
A = M[12].inverse()
B = M[13].inverse()

print((A * B) ** -1)
print((A.transpose() ) ** -1)
print((A*2 ) ** -1)

probno(12)
A = ltr(2, 1, 2, 1, -2)
B = ltr(2, 1, 2, 1, -2)

print(A **-1 *  Matrix([[1, -3]]).transpose() )
print(B **-1 *  Matrix([[10, -6]]).transpose() )

probno(13)
A = ltr(3, 1, 2, 1, 1, 2, -1, 1, -2, 1)
print(A **-1 *  Matrix([[2, 0, -2]]).transpose() )
print(A **-1 *  Matrix([[-1, -3, 3]]).transpose() )

probno(16)
print((M[14] * 4).inverse() )


