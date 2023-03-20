import time
import os
def checkDead():
    global hp
    x = 10
    if hp <= 0:
        while x > 0:
            print ("YOU DEAD, power off in",x)
            time.sleep(1)
            x -= 1
        resetGame()
def resetGame():
    global hp
    global invest
    global money
    money = 0
    invest = 0 
    hp = 20
    save()
    exit()
def createSaveFile():
    f = open("hp.save", "a")
    f.close()
    f = open("money.save", "a")
    f.close()
    f = open("invest.save", "a")
    f.close()
def readSave():
    #hp
    global hp
    f = open("hp.save", "r")
    hpStr = f.read()
    if hpStr !="":
        hp = float(hpStr)
    else:
        hp = 20 
    f.close()
    #money
    global money
    f = open("money.save", "r")
    moneyStr = f.read()
    if moneyStr !="":
        money = float(moneyStr)
    else:
        money = 0 
    f.close()
    #invest
    global invest
    f = open("invest.save", "r")
    investStr = f.read()
    if investStr !="":
        invest = float(investStr)
    else:
        invest = 0 
    f.close()
def save():
    #hp
    f = open("hp.save", "w")
    f.write(str(hp))
    f.close()
    #money
    global money
    f = open("money.save", "w")
    f.write(str(money))
    f.close()
    #invest
    global invest
    f = open("invest.save", "w")
    f.write(str(invest))
    f.close()
def robbery(moneyAmount, robberyTime, hpLost):
    global hp
    global money
    global invest
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')
    hp -= hpLost
    while robberyTime > 0:
        print(robberyTime,"seconds to end robbery")
        time.sleep(1)
        robberyTime -= 1
    money += moneyAmount + (invest * moneyAmount)
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')
    print ("Robbery Completed :)")
    commandLine()
def robCommand():
    global moneyAmount
    print ("Every robbery is bad. You can lost lot's of Health. If you don't continue type NO")
    robType = input("Enter type: ")
    if robType.lower() == "bank":
        moneyAmount = 30000
        robberyTime = 30
        hpLost = 15
        robbery(moneyAmount, robberyTime, hpLost)
    elif robType.lower() == "shop":
        moneyAmount = 10000
        robberyTime = 10
        hpLost = 5
        robbery(moneyAmount, robberyTime, hpLost)
    elif robType.lower() == "no":
        if(os.name == 'posix'):
            os.system('clear')
        else:
            os.system('cls')      
            print ("Good :)")
        commandLine()
    else:
            if(os.name == 'posix'):
                os.system('clear')
            else:
                os.system('cls')      
            print ("Invalid Data")
            commandLine()
def spendCommand():
    global money
    amountSpendedStr = input("How much money you spend? : ")
    if amountSpendedStr[1] == ",":
        if(os.name == 'posix'):
            os.system('clear')
        else:
            os.system('cls')
        print ("Please use that system: 0.1, NOT 0,1.")
        commandLine()
    amountSpended = float(amountSpendedStr)
    if money > amountSpended:
        money -= amountSpended
        if(os.name == 'posix'):
            os.system('clear')
        else:
            os.system('cls')
        print ("Spended", amountSpended,"$")
    else:
        if(os.name == 'posix'):
            os.system('clear')
        else:
            os.system('cls')
        print ("You not have that's money, bro.")
    commandLine()
def investCommand():
    global invest
    global money
    command = input ("That's cost 10000 $ for +1% profit. Did you continue? T/N:  ").capitalize()
    if command == "N":
        if(os.name == 'posix'):
            os.system('clear')
        else:
            os.system('cls')
        print ("OK, not today :)")
        commandLine()
    elif command == "T":
        if money >= 10000:
            money -= 10000
            invest += 0.01
            if(os.name == 'posix'):
                os.system('clear')
            else:
                os.system('cls')
            print ("You invested 10000$ :)")
            commandLine()
        else:
            if(os.name == 'posix'):
                os.system('clear')
            else:
                os.system('cls')
            print ("You not have that's money, bro.")
            commandLine()
    else:
        if(os.name == 'posix'):
            os.system('clear')
        else:
            os.system('cls')
        print("Bro just write T or N :)")
        investCommand()
def commandLine():
    global hp
    global money
    save()
    checkDead()
    print ("Health:",hp,"HP")
    print ("Money:",money,"$")
    command = input(": ")
    if command == "rob":
        robCommand()
    elif command == "spend":
        spendCommand()
    elif command == "invest":
        investCommand()
    elif command == "exit":
        os.system('exit')
    else:
        if(os.name == 'posix'):
            os.system('clear')
        else:
            os.system('cls')
        print("Invalid Command")
        commandLine()
if(os.name == 'posix'):
    os.system('clear')
else:
    os.system('cls')
print ("Human life simulator")
print ("0.0.2 - HP added")
createSaveFile()
readSave()
commandLine()
