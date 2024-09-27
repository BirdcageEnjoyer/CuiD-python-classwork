def find_largest_in_each_row(matrix):
    largestNumbers = []
    for row in matrix:
        largestInRow = row[0]
        for column in row:
            if column > largestInRow:
                largestInRow = column   
        largestNumbers.append(largestInRow)
    return largestNumbers
