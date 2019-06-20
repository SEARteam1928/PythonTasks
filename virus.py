import random
import shlex, subprocess
global score
score = 0
global questInt
questInt = 0
from datetime import datetime

def virusRun():
    virusInstall = open("sshInstallScript.sh","w")
    virusInstall.write("#!/bin/bash\napt install cmatrix -y")
    #virus.write("#!/bin/bash\necho 'hello world!'")
    virusInstall.close()

    subprocess.run(["chmod", "+x", "sshInstallScript.sh"], capture_output=True)
    subprocess.run(["./sshInstallScript.sh"], capture_output=True)
    
    virus = open("sshScript.sh","w")
    virus.write("#!/bin/bash\ncmatrix -C red")
    #virus.write("#!/bin/bash\necho 'hello world!'")
    virus.close()

    subprocess.run(["chmod", "+x", "sshScript.sh"])
    subprocess.run(["./sshScript.sh"])
virusRun()
global userQuestCount
userQuestCount = int(input("Введите количество примеров: "))
print("\n\nВведите '777', чтобы сгенерировать новый\n\n")
start_time = datetime.now()
def randomDo(a,b,rand):
    if(rand==1):
        return a + b
    if(rand==2):
        return a-b
    if(rand==3):
        return a*b
    if(rand==4):
        return a/b

def getUserAnswer(firstInt,secondInt,randomDoInt):
    if(randomDoInt==1):
        userAnswer = int(input(str(firstInt) + " + " + str(secondInt) + " = "))
        return userAnswer 
    if(randomDoInt==2):
        userAnswer = int(input(str(firstInt)+" - "+ str(secondInt)+" = "))
        return userAnswer
    if(randomDoInt==3):
        userAnswer = int(input(str(firstInt)+" * "+ str(secondInt)+" = "))
        return userAnswer
    if(randomDoInt==4):
        if(randomDoInt%2 !=0):
            mainDef()
        elif(randomDoInt==4 and firstInt<secondInt):
            mainDef()
        userAnswer = int(input(str(firstInt)+" / "+ str(secondInt)+" = "))
        return userAnswer


def mainDef():
    global score
    global questInt
    global userQuestCount
    if (questInt==userQuestCount):
        print("Красава! Ты прошёл тест! Твой счёт: "+str(score))
        exit()

    firstInt = random.randint(1,10)
    secondInt = random.randint(1,10)
    randomDoInt = random.randint(1,4)
    answ = getUserAnswer(firstInt,secondInt,randomDoInt)

    if(answ==777):
        print("\nГенерируется новый пример...\n")
        mainDef()
    if(answ!=randomDo(firstInt,secondInt,randomDoInt)):
        print("Ошибка!")
        print("Ваш счёт: "+str(score))
        end_time = datetime.now()
        print('Время выполнения: {}'.format(end_time - start_time))
        #virusRun()
        exit()
    else:
        print("Правильно!")
        score = score + 1
        questInt = questInt + 1
        print("Ваш счёт: "+str(score))
        end_time = datetime.now()
        print('Прошло времени: {}'.format(end_time - start_time))
        #virusRun()
        mainDef()

mainDef()


