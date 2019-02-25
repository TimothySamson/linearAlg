from linear import *

def ltr(colNum, *arg):
    return Matrix([list(arg[i*colNum : (i+1)*colNum])
        for i in range(int(len(arg) / colNum))])

def probno(num):
    print("------- Problem number ", num)

print(refElemList(ltr(3, 1, -2, -1, 0, 3, 6, -6, 12, 9)))

