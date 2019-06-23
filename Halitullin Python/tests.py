import random
from tasks.task1 import *
from tasks.task2 import *

def selectTask(selectInt):
    if(selectInt==1):
        test1()
    if(selectInt==2):
        test2()
    else:
        print("\nЕсли задание не включается, то либо вы что-то написали неправильно, либо Газинур не сделал это задание!\n")

def test1():
    arrayin = []
    lengthInt = random.randint(1,100)
    for count in range(lengthInt):
        forStr = str(random.randint(1,100))
        forStrAndNull = forStr+"0"
        forInt = int(str(forStrAndNull))
        arrayin.append(forInt)
    task1(arrayin)

def test2():
    arrayin = []
    lengthInt = random.randint(1,100)
    for count in range(lengthInt):
        forInt = random.randint(1,100)
        arrayin.append(forInt)
    arrayin.append(random.randint(-100, -1))
    task2(arrayin)
