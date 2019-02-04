import linear

class functionMixin:
    def transpose(matrix):
        return linear.Matrix([matrix.getCol(i) for i in range(matrix.colNum())])


    def subMatrix(self, slice1, slice2):
        return linear.Matrix([row[slice2] for row in self[slice1]])

    

    # # Using minor expansion
    # def determinant(matrix):
        # sign = 1
        # for num in
        
            
    # # Using cofactors
    # def inverse(matrix):
