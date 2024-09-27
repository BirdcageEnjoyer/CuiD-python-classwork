def matrix_diagonal_difference(matrix):
    firstDiagonal = 0
    secondDiagonal = 0
    length = len(matrix)
    position = 0
    positionReverse = length - 1
    for row in matrix:
        firstDiagonal += row[position]
        position += 1
    for row2 in matrix:
        secondDiagonal += row2[position]
        positionReverse -= 1
    difference = firstDiagonal - secondDiagonal
    if difference < 0:
        difference *= -1
    return difference