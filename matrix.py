class Matrix:
    def __init__(self, array):
        dimension = len(array[0])
        for row in array:
            if len(row) != len(row):
                raise ValueError("Mismatch of dimensions")

        self.array = array
    
    def cols(self):
        return len(self.array[0])

    def rows(self):
        return len(self.array)

    def __mul__(self, right):
        if self.cols() != right.rows():
            raise ValueError("Mismatch of dimensions")
        matrix = []
        for leftRow in self.array:
            row = []
            for rightRow in right.transpose().array:
                num = 0
                for i in range(len(rightRow)):
                    num += rightRow[i] * leftRow[i]
                row.append(num)
            matrix.append(row)

        return Matrix(matrix)

    def __str__(self):
        return "\n".join((str(a) for a in self.array)) + "\n"

    def transpose(self):
        dimension = len(self.array[0])
        newMatrix = []
        for rowNum in range(dimension):
            vector = [row[rowNum] for row in self.array]
            newMatrix.append(vector)
        
        return Matrix(newMatrix)

array = [
[0, 0, 0, 0], 
[0, 1, 0, 0], 
[0, 0, 0, 0], 
[0, 0, 0, 0]]

a = Matrix(array)

array = [
[1, 2, 3, 4], 
[5, 6, 7, 8], 
[0, 0, 3, 0], 
[0, 0, 0, 4]]
b = Matrix(array)

print(a)
print(b)
print(a * b)
