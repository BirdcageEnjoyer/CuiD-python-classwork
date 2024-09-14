end = False
totalTest1 = 0
totalTest2 = 0
totalTest3 = 0
for i in range(0, 30):
    test1 = int(input("enter person", i + "'s test 1 score"))
    test2 = int(input("enter person", i + "'s test 2 score"))
    test3 = int(input("enter person", i + "'s test 3 score"))
    totalTest1 += test1
    totalTest2 += test2
    totalTest3 += test3

averageT1 = totalTest1/30
averageT2 = totalTest2/30
averageT3 = totalTest3/30
totalAvg = (averageT1 + averageT2 + averageT3) / 3

print(averageT1, averageT2, averageT3, totalAvg)



