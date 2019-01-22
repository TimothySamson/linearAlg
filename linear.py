from fractions import Fraction as Frac

class Vector:
    def __init__(self, array):
        self.array = array.copy()
    
    def __add__(self, vect2):
        if len(vect2) != len(self):
            raise ValueError("Adding vectors with different dims")

        newArray = []
        for i in range(len(vect2)):
            newArray.append(self.array[i] + vect2.array[i])

        return Vector(newArray)
    def __sub__(self, vect2):
        return self + (-1) * vect2

    def __mul__(self, num):
        # Dot Product if vecror, scalar mult if num
        if isinstance(num, Vector):
            if len(self) != len(num):
                raise ValueError("dot product error: len mismatch")
            return sum([num[i] * self[i] for i in range(len(self))])
        return Vector([num * x for x in self.array])

    def __len__(self):
        return len(self.array)

    def __rmul__(self, num):
        return self * num

    def __truediv__(self, num):
        return self * (1/num)

    def __str__(self):
        return str(self.array)

    def __getitem__(self, index):
        return self.array[index]

    def copy(self):
        return self.array.copy()

class Matrix:
    def __init__(self, array):
        dim = len(array[0])
        newArray = []
        for row in array:
            if len(row) != dim:
                raise ValueError("Mismatch of matrix creation dimension")
            newArray.append(Vector(row))

        self.array = newArray

    def rowNum(self):
        return len(self.array)

    def colNum(self):
        return len(self.array[0])
    
    # IN PLACE
    def swapRow(self, x, y):
        self.array[x], self.array[y] = self.array[y], self.array[x]

    def copy(self):
        return Matrix(self.array)
            
    def __str__(self):
        return "\n".join([str(row) for row in self])

    def __getitem__(self, index):
        return self.array[index]

    def fracStr(self):
        matrix = self.copy()
        string = ""
        newRow = []
        for row in matrix:
            row = [Frac(x).limit_denominator() for x in row]
            for x in row:
                if x.numerator == 0:
                    newRow.append("0")
                    continue
                if x.denominator == 1:
                    newRow.append(str(x.numerator))
                    continue
                
                newRow.append(f"{x.numerator}/{x.denominator}")
            
            string += str(newRow) + "\n"
            newRow = []
        return string

    def getCol(self, num):
        return Vector([row[num] for row in self])

    def __mul__(self, matrix2):
        if self.colNum() != matrix2.rowNum():
            raise ValueError("mult matrix error: dim mismatch")
        
        matrix1 = self

        newArray = []
        row = []
        for i in range(matrix1.rowNum()):
            for j in range(matrix2.colNum()):
                row.append(matrix1[i] * matrix2.getCol(j))

            newArray.append(row)
            row = []

        return Matrix(newArray)

    def __add__(self, matrix2):
        if self.rowNum() != matrix2.rowNum():
            raise ValueError("adding matrix error: row mismatch")
        if self.colNum() != matrix2.colNum():
            raise ValueError("adding matrix error: column mismatch")
        
        newArray = []
        for i in range(self.rowNum()):
            newArray.append(self[i] + matrix2[i])

        return Matrix(newArray)

def ref(matrix):
    matrix = matrix.copy()
    for i in range(matrix.rowNum()):
        pivot = matrix.array[i][i]

        # Finds a non-zero num on the same column, and swaps if it finds it
        if Frac(pivot).limit_denominator().numerator == 0:
            for j in range(i+1, matrix.rowNum()):
                if matrix.array[j][i] != 0:
                    matrix.swapRow(j, i)
                    break
        
        # if the pivot is still zero, then that must mean there is no nonzero 
        # num in the column, so skip it
        pivot = matrix.array[i][i]
        if Frac(pivot).limit_denominator().numerator == 0:
            continue
        
        # Make current row have a pivot of zero
        matrix.array[i] = matrix.array[i] / pivot
        
        # Make all other rows zero
        for j in range(i+1, matrix.rowNum()):
            matrix.array[j] = matrix[j] - matrix[i] * matrix[j][i]

    return matrix

# Assuming all pivots are one
def backSubstitute(matrix):
    matrix = matrix.copy()

    for i in range(matrix.rowNum() - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            matrix.array[j] = matrix[j] - matrix[i] * matrix[j][i]
            # print (i, j)

    return matrix

