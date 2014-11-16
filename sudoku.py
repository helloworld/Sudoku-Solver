class Cell(object):
    """Individual Cells in the Matrix"""
    def __init__(self, val, r, c, matrix):
        if (val != 0):
            self.value = {val, }
        else:
            self.value = {1, 2, 3, 4, 5, 6, 7, 8, 9, }
        self.row = r
        self.col = c
        self.block = blockNumber(r, c)
        self.matrix = matrix
        
def blockNumber(row, col):
    if row < 3 and col < 3:
        return 0
    if row < 3 and 2 < col < 6:
        return 1
    if row < 3 and 5 < col:
        return 2
    if 2 < row < 6 and col < 3:
        return 3
    if 2 < row < 6 and 2 < col < 6:
        return 4
    if 2 < row < 6 and 5 < col:
        return 5
    if row > 5 and col < 3:
        return 6
    if row > 5 and 2 < col < 6:
        return 7
    if row > 5 and 5 < col:
        return 8

def createTheSudokuBoard():
    M = [
        [4, 8, 1, 5, 0, 9, 6, 7, 0, ],
        [3, 0, 0, 8, 1, 6, 0, 0, 2, ],
        [5, 0, 0, 7, 0, 3, 0, 0, 8, ],
        [2, 0, 0, 0, 0, 0, 0, 0, 9, ],
        [9, 0, 0, 0, 0, 0, 0, 0, 1, ],
        [8, 0, 0, 0, 0, 0, 0, 0, 4, ],
        [0, 3, 9, 2, 7, 5, 4, 8, 0, ],
        [6, 0, 0, 0, 0, 0, 9, 2, 7, ],
        [7, 0, 0, 0, 0, 0, 3, 1, 0, ]
    ]
    matrix = []
    for r in range(9):
        row = []
        for c in range(9):
            row.append(Cell(M[r][c], r, c, matrix))
        matrix.append(row);
    return matrix

def main():
    matrix = createTheSudokuBoard();
    print(matrix)
    
if __name__ == '__main__':
    main()