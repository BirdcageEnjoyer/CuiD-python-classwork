def sum_rows(matrix):
    totalRowSumsArray = []
    for row in matrix:
        sum = 0
        for column in row:
            sum += column
        totalRowSumsArray.append(sum)
    return totalRowSumsArray