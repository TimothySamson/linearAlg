from linear import *
import re

# List of tuples
def polynomial(points):
    rowLen = len(points)
    matrix = [[point[0] ** i for i in range(rowLen)] + [point[1]] 
             for point in points]
    matrix = Matrix(matrix)
    return matrix.rref()

# List of lists
# Solving the equation nodes[0] = 0, nodes[1] = 0, ...
def parseVar(string):
    temp = list(re.split(r'[a-zA-Z]+', string))
    if temp[0] == "-":
        temp[0] = -1 
    if temp[0] == "":
        temp[0] = 1
    
    return tuple([int(x) for x in temp])
    
def flow(nodes):
    # variables = [[int(''.join(x for x in var if x in "-1234567890")) 
            # for var in eq if isinstance(var, str)]
            # for eq in nodes]
    variables = [[parseVar(var)
            for var in eq if isinstance(var, str)] 
            for eq in nodes]
    augmented = [-sum([num for num in eq if not isinstance(num, str)])
            for eq in nodes]
    
    colLen = max([abs(var[1]) for var in sum(variables, [])]) 

    matrix = []
    for i in range(len(augmented)): 
        row = [0] * colLen + [augmented[i]]
        
        for var in variables[i]:
            row[var[1] - 1] = var[0]
            # if var < 0:
                # row[-var - 1] = -1
            # else: 
                # row[var - 1] = 1

        matrix.append(row)
        row = []

    matrix = Matrix(matrix)

    return Matrix(matrix)


print("Problem 1")
matrix = flow([
[400, "x2", "-x1"],
["x3", "x1", "-x4", -600],
[300, "-x2", "-x3", "-x5"],
["x5", "x4", -100]
    ])
print(matrix.rref())
print("\n")

print("Problem 2")
matrix = flow([
["x2", 400, "-x1"],
[100, "x1", "-x3"],
["x3", -400, 0],
[0, "-x2", -100]])
# print(matrix)
# print("\n")
print(matrix.rref())
print("\n")

print("Problem 3")

matrix = flow([
[800, "-x1", "-x3"],
["x1", "-x2", "-x4"],
[-700, "x2", "x5"],
["x6", "x3", -800],
["x7", "x4", "-x6"],
[700, "-x7", "-x5"]
    ])
print(matrix)
print("\n")
print(matrix.rref())
print("\n")

# Problem 3
# [-1, 0, -1, 0, 0, 0, 0, -900]
# [1, -1, 0, -1, 0, 0, 0, 0]
# [0, 1, 0, 0, 1, 0, 0, 400]
# [0, 0, 1, 0, 0, 1, 0, 900]
# [0, 0, 0, 1, 0, -1, 1, 0]
# [0, 0, 0, 0, -1, 0, -1, -400]


# [1.0, 0.0, 0.0, 0.0, 0.0, -1.0, 0.0, 0.0]
# [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, -1.0, 0.0]
# [0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 900.0]
# [0.0, 0.0, 0.0, 1.0, 0.0, -1.0, 1.0, 0.0]
# [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 400.0]
# [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

print("Problem 4")

matrix = flow([
[3, "-4I1", "-3I2"],
[4, "-I3", "-3I2"],
["I1", "I3", "-I2"]
    ])

print(matrix)
print("\n")
print(matrix.rref())
print("\n")

# [1.0, 0.0, 0.0, 0.0]
# [-0.0, 1.0, 0.0, 1.0]
# [0.0, 0.0, 1.0, 0.9999999999999999]


print(Matrix([
    [100, -10, 1, 242],
    [0, 0, 1, 285],
    [100, 10, 1, 322]
]).rref())
