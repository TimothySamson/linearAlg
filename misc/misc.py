import linear

def refElemList(matrix):
    matrix = matrix.copy()
    size = matrix.rowNum()
    matrixList = []
    for i in range(matrix.rowNum()):
        pivot = matrix.array[i][i]

        if pivot == 0:
            for j in range(i+1, matrix.rowNum()):
                if matrix.array[j][i] != 0:
                    matrix.swapRow(j, i)
                    matrixList.insert(0, elemSwap(size, i, j))
                    break
        
        pivot = matrix.array[i][i]
        if pivot == 0:
            continue
        
        matrix.array[i] = matrix.array[i] / pivot
        if pivot != 1:
            matrixList.insert(0, elemMul(size, i, 1/pivot))
        
        for j in range(i+1, matrix.rowNum()):
            matrix.array[j] = matrix[j] - matrix[i] * matrix[j][i]
            print("Hello")
            if matrix[j][i] != 0:
                print("Hello")
                matrixList.insert(0, elemAdd(size, i, j, -matrix[j][i]))

    string = ""
    for row in range(size):
        for matrix in matrixList:
            string += str(matrix.fracStr()[row])
        string += "\n"

    return string

def elem(size):
    return linear.Matrix([
            [1 if col == row else 0 for col in range(size)] 
            for row in range(size)])

def elemSwap(size, i, j):
    matrix = elem(size)
    matrix.swapRow(i, j)
    return matrix

# add row i to row j
def elemAdd(size, i, j, mul=1):
    matrix = elem(size)
    matrix[j] = matrix[i]*mul + matrix[j]
    return matrix

def elemMul(size, i, num):
    matrix = elem(size)
    matrix[i] = matrix[i] * num
    return matrix
