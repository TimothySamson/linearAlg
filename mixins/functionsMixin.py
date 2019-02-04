import linear

class functionMixin:
    def transpose(matrix):
        return linear.Matrix([matrix.getCol(i) for i in range(matrix.colNum())])


    def subMatrix(self, slice1, slice2):
        return linear.Matrix([row[slice2] for row in self[slice1]])
    
    def minor(self, row, col):
        return linear.Matrix([[self[j][i]
                            for i in range(self.colNum())
                                if i != col] 
                            for j in range(self.rowNum())
                                if j != row])

    def det(matrix):
        if matrix.colNum() != matrix.rowNum():
            raise ValueError("determinant of nonsquare matrix")
        dim = matrix.colNum()

        if dim == 1:
            return matrix[0][0]

        sign = 1
        val = 0
        for i in range(dim):
            val += sign * matrix[0][i] * matrix.minor(0, i).det()
            sign *= -1

        return val

    def cofactor(matrix):
        return linear.Matrix([[(-1)**(i+j) * matrix.minor(j, i).det()
                            for i in range(matrix.colNum())]
                            for j in range(matrix.rowNum())])

    # Using cofactors
    def inverse(matrix):
        return matrix.det()**(-1) * matrix.cofactor().transpose()

    def trace(matrix):
        return sum([matrix[a][a] for a in range(matrix.colNum())])
