from bs4 import BeautifulSoup

import sys
sys.path.append("..")

from linear import *

def html2matrix(string):
    soup = BeautifulSoup(string, "html.parser")
    tables = soup.findAll("table", {"class": "watexmatrix"})
    
    matrices = []
    for table in tables:
        matrix = []
        for row in table.tbody.findChildren("tr", recursive=False):
            matrixRow = []
            for data in row.findChildren("td", recursive=False):
                if "watexmatrixparen" not in data["class"]:
                    num = data.getText().strip()
                    if num[0] in "-−":
                        num = -float(num[1:])
                    num = float(num)
                    matrixRow.append(num)
            matrix.append(matrixRow)

        matrices.append(Matrix(matrix))

    return matrices

