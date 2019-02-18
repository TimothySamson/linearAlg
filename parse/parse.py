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
                    try:
                        num = data.getText().strip()
                        if num[0] in "-−":
                            num = -float(num[1:])
                        num = float(num)
                        matrixRow.append(num)
                    except Exception:
                        continue
            matrix.append(matrixRow)
        
        if not matrix[0]:
            continue

        try:
            matrices.append(Matrix(matrix))
        except:
            continue

    return matrices

