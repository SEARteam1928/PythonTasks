def task1(arrayInt):
    print("Создана Последовательность чисел: ", str(arrayInt))
    i = 0
    allIntSum = 0
    for intInFor in arrayInt:
        allIntSum += int(intInFor)
        i += 1
    print("Сумма чисел Последовательности равна:\n", allIntSum, "\n")
    print("Количество чисел в Последовательности:\n", len(arrayInt), "\n")

