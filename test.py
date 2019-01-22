from linear import * 
from fractions import Fraction as Q

matrix = [
[0,1,1,-2,-3],
[1, 2, -1,0, 2],
[2, 4, 1, -3, -2],
[1, -4, -7, -1, -19]]

# ---- REF 
matrix = Matrix(matrix)

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
