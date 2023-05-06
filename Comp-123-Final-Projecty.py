import csv
import string

def readCSV(filename):
    dataIn = open(filename, 'r')
    csvReader = csv.DictReader(dataIn)
    fields = csvReader.fieldnames
    table = []
    for rowDict in csvReader:
        table.append(rowDict)
    dataIn.close()
    return fields, table

PDfield, PDtable = readCSV('C:/Users/benki/Downloads/stats.csv')

def isNumber(myString):
    """
    Function which takes a string as input and returns True if it can be interpreted as a number.
    i.e. converted into a float (and also therefore an int)
    """
    try:
        float(myString)
        return True
    except ValueError:
        return False



def isLucky(luck):
    if luck < -6:
        return " is very lucky"
    if luck < -2:
        return " is lucky"
    if luck < 2:
        return " is not lucky or unlucky"
    if luck < 6:
        return " is unlucky"
    else:
        return " is very unlucky"

def newPlayer():
    ba = input("What is their batting average against? ")
    while isNumber(ba) != True:
        print("Please enter a valid number")
        ba = input("What is their batting average against? ")
    ba = float(ba)

    xba = input("What is their expected batting average against? ")
    while isNumber(xba) != True:
        print("Please enter a valid number")
        xba = input("What is their expected batting average against? ")
    xba = float(xba)

    slg = input("What is their slugging against? ")
    while isNumber(slg) != True:
        print("Please enter a valid number")
        slg = input("What is their slugging against? ")
    slg = float(slg)

    xslg = input("What is their expected slugging against? ")
    while isNumber(xslg) != True:
        print("Please enter a valid number")
        xslg = input("What is their expected slugging against? ")
    xslg = float(xslg)

    woba = input("What is their weighted on base average against? ")
    while isNumber(woba) != True:
        print("Please enter a valid number")
        woba = input("What is their weighted on base average against? ")
    woba = float(woba)

    xwoba = input("What is their expected weighted on base average against? ")
    while isNumber(xwoba) != True:
        print("Please enter a valid number")
        xwoba = input("What is their expected weighted on base average against? ")
    xwoba = float(xwoba)

    luckstat = ((ba-xba) + (slg - xslg) + (woba - xwoba)) * 100
    return luckstat

def luckstat(xbadiff, xslgdiff, wobadiff):
    luckstat = (xbadiff + xslgdiff + wobadiff) * 100
    return luckstat

def findplayer():
    playerfirst = input("Input Player First Name: ")
    playerlast = input("Input Player Last Name: ")
    for row in PDtable:
        if playerlast.strip().lower() == row['ï»¿last_name'].strip().lower() and \
                playerfirst.strip().lower() == row[' first_name'].strip().lower():
            print(playerfirst.strip().capitalize() + ' ' + playerlast.strip().capitalize() +
                  isLucky(luckstat(float(row['xbadiff']), float(row['xslgdiff']), float(row['wobadiff']))))
            return
    luck = newPlayer()
    print(playerfirst.strip() + ' ' + playerlast.strip() + isLucky(luck))

def finalFunction():
    yesorno = "yes"
    while yesorno == "yes" or yesorno == "Yes":
        findplayer()
        yesorno = input("Would you like to keep going? ")
        while yesorno != "Yes" and yesorno != "No" and yesorno != "yes" and yesorno != "no":
            print("Please enter Yes or No")
            yesorno = input("Would you like to keep going? ")
    print("Thank you and have a lucky day!")

finalFunction()