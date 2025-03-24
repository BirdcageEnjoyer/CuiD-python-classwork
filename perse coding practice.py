matrixA = []
matrixB = []
for i in range(3):
    matrixA.append(input().split(","))
for i in range(3):
    matrixB.append(input().split(","))
    
# print("--------------")
# for i in matrixA:
#     print(','.join(i))
# for i in matrixB:
#     print(','.join(i))

matrixC = [[],[],[]]
for i in range(3):
    for x in range(3):
        for y in range(3):
            matrixA[i][y] * matrixB[y][x]
