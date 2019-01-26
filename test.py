from linear import * 
from fractions import Fraction as Q

matrix = [
[0,1,1,-2,-3],
[1, 2, -1,0, 2],
[2, 4, 1, -3, -2],
[1, -4, -7, -1, -19]]
matrix = Matrix(matrix)

# ---- REF 

print(ref(matrix).fracStr())

# ---- backSubstitute
print(backSubstitute(ref(matrix)).fracStr())

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
print(backSubstitute(ref(matrix)))


print("\n")
matrix = [
[4, 12, -7, -20, 20],
[3, 9, -5, -28, 30]]
matrix = Matrix(matrix)
print(backSubstitute(ref(matrix)))


print("\n")
matrix = [
[1.0, 3.0, -1.75, -5.0, 5.0],
[0.0, 0.0, 0.25, -13.0, 15.0]]
matrix = Matrix(matrix)
print(Matrix([matrix[0] + matrix[1] * 7, matrix[1]]))
