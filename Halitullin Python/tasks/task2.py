def task2(arrayInt):
    print("\nСоздана последовательность: ", arrayInt)
    arythLen = len(arrayInt) - 1
    arythSum = 0
    for i in range(arythLen):
        arythSum = arythSum+arrayInt[i]
    aryth = int(arythSum / arythLen)
    print("\nКоличество положительных чисел в последовательнсти: ", arythLen)
    print("Среднее арифметическое последовательности: ", aryth, "\n")
