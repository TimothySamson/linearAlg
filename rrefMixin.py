import linear

class rrefMixin:
    def ref(matrix):
        matrix = matrix.copy()
        for i in range(matrix.rowNum()):
            pivot = matrix.array[i][i]

            # Finds a non-zero num on the same column, and swaps if it finds it
            if pivot == 0:
                for j in range(i+1, matrix.rowNum()):
                    if matrix.array[j][i] != 0:
                        matrix.swapRow(j, i)
                        break
            
            # if the pivot is still zero, then that must mean there is no nonzero 
            # num in the column, so skip it
            pivot = matrix.array[i][i]
            if pivot == 0:
                continue
            
            # Make current row have a pivot of zero
            matrix.array[i] = matrix.array[i] / pivot
            
            # Make all other rows zero
            for j in range(i+1, matrix.rowNum()):
                matrix.array[j] = matrix[j] - matrix[i] * matrix[j][i]

        return matrix

    def backSubstitute(matrix):
        matrix = matrix.copy()

        for i in range(matrix.rowNum() - 1, 0, -1):
            if matrix[i][i] == 0:
                continue
            for j in range(i - 1, -1, -1):
                matrix.array[j] = matrix[j] - matrix[i] * matrix[j][i]
                # print (i, j)

        return matrix

    def rref(matrix):
        return matrix.ref().backSubstitute()


