import random
from tasks.task1 import *

def test1():
    arrayin = []
    lengthInt = random.randint(2,100)
    for count in range(lengthInt):
        forStr = str(random.randint(2,100))
        forStrAndNull = forStr+"0"
        forInt = int(str(forStrAndNull))
        arrayin.append(forInt)
    task1(arrayin)
