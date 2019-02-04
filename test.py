from linear import * 
from fractions import Fraction as Q

matrix = [
[0,1,1,-2,-3],
[1, 2, -1,0, 2],
[2, 4, 1, -3, -2],
[1, -4, -7, -1, -19]]
matrix = Matrix(matrix)

# ---- REF 

print(matrix.ref().fracStr())

# ---- backSubstitute
print(matrix.backSubstitute().fracStr())

# ---- Get Column
print(matrix.getCol(1))

# ---- Matrix mult
matrix1 = [
[1, 1, 1],
[1, 2, 1],
[1, 1, 3]]
matrix1 = Matrix(matrix1)
print(matrix1 * matrix1)

matrix = [
[2, 4, -2, 2],
[4, 6, 0, 0],
[0, 0, 0, 4]]
matrix = Matrix(matrix)

print("\n")
print(matrix.ref().backSubstitute())


print("\n")
matrix = [
[4, 12, -7, -20, 20],
[3, 9, -5, -28, 30]]
matrix = Matrix(matrix)
print(matrix.rref())


print("\n")
matrix = [
[1.0, 3.0, -1.75, -5.0, 5.0],
[0.0, 0.0, 0.25, -13.0, 15.0]]
matrix = Matrix(matrix)
print(Matrix([matrix[0] + matrix[1] * 7, matrix[1]]))

matrix1 = Matrix([
[-1 , 3],
[4, -2],
[5, 0]])

matrix2 = Matrix([
[-3, 2],
[-4, 1]])

print("\n")
print(matrix1 * matrix2)

matrix1 = Matrix([
[1, 0, 3],
[2, -1, -2]
])
matrix2 = Matrix([
[-2, 4, 2],
[1, 0, 0],
[-1, 1, -1]
    ])

print("\n")
print(matrix1 * matrix2)

print("Transpose")
print(Matrix(([[1, 2, 3, 4]])).transpose())
