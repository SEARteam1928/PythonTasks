from tests import *


def mainDef():
    selectNum = int(input("Введите номер нужного задания от 1 до 46: \n"))
    selectTask(selectNum)
    mainDef()
mainDef()

