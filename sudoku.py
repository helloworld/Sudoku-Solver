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
    def __str__(self):
        if (len(self.value) > 1):
            return '0'
        else:
            element = min(self.value)
            return str(element)

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

def printMatrix(matrix):
    print()
    for x in matrix:
        print()
        for y in x:
            print(y, end=" ")
    print()
    numberOfEmptySells(matrix)
    print()

def checkRowsAndColumns(matrix):
    while True:
        (matrix, condition) = checkRowsAndColumnsHelper(matrix)
        if(condition == True):
            return matrix;

def checkRowsAndColumnsHelper(matrix):
    for x in range(9):
        for y in range(9):
            if(len(matrix[x][y].value)>1):
                for i in range(9):
                    currentCell = matrix[x][i]
                    if(len(currentCell.value) == 1):
                        matrix[x][y].value -= currentCell.value
                        if(len(matrix[x][y].value) ==1):
                            # print(x, y, "changed to", matrix[x][y].value)
                            return (matrix, False)
                for j in range(9):
                    currentCell = matrix[j][y]
                    if(len(currentCell.value) == 1):
                        matrix[x][y].value -= currentCell.value
                        if(len(matrix[x][y].value) ==1):
                            # print(x, y, "changed to", matrix[x][y].value)
                            return (matrix, False)
    return (matrix, True)


def getBlocks(matrix):
    block = [[],[],[], [],[],[], [],[],[],]
    for x in range(9):
        for y in range(9):
            currentBlock = blockNumber(x,y)
            block[currentBlock].append(matrix[x][y].value)
    return block

def checkBlocks(matrix):
    while True:
        (matrix, condition) = checkBlocksHelper(matrix)
        if(condition == True):
            return matrix;
        else:
            matrix = checkRowsAndColumns(matrix)


def checkBlocksHelper(matrix):
    blocks = getBlocks(matrix)
    for x in range(9):
        for y in range(9):
            if(len(matrix[x][y].value)>1):
                currentBlock = blockNumber(x,y)
                for currentCell in blocks[currentBlock]:
                    if(len(currentCell) ==1):
                        matrix[x][y].value -= currentCell
                    if(len(matrix[x][y].value) ==1):
                        # print(x, y, "changed to", matrix[x][y].value)
                        return (matrix, False)
    return (matrix, True)

def allCellsHaveValues(matrix):
    for x in range(9):
        for y in range(9):
            if(matrix[x][y].value == set()):
                return False
    else:
        return True

def numberOfEmptySells(matrix):
    count = 0
    for x in range(9):
        for y in range(9):
            if(len(matrix[x][y].value) > 1):
                count+=1
    else:
        print("Number of Empty Cells:", count)

def reduceMatrix(matrix):
    matrix = checkRowsAndColumns(matrix)
    matrix = checkBlocks(matrix)
    return matrix

def main():
    matrix = createTheSudokuBoard();
    matrix = reduceMatrix(matrix)
    printMatrix(matrix)

    print("All Cells Have Values:", allCellsHaveValues(matrix))
    
if __name__ == '__main__':
    main()