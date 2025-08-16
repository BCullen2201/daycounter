#!/usr/bin/env python3

from os import system
from os import makedirs
from sys import exit
from datetime import date
from os.path import exists
from getpass import getuser

mainMenu = """Day Counter
=======================
1 - Set start date
2 - Exit
=======================
"""

userName = getuser()

today = date.today()
currentMonth = int(today.strftime("%m"))
currentDay = int(today.strftime("%d"))
currentYear = int(today.strftime("%Y"))

startDateFromDisk = None

def continuePrompt(continuePromptMsg):
    input(f"\n{continuePromptMsg}")

def getDateFromDisk():
    with open(f"/home/{userName}/.local/share/daycounter/date", "r") as getDate:
        year = getDate.readline().rstrip()
        month = getDate.readline().rstrip()
        day = getDate.readline().rstrip()

    global startDateFromDisk
    startDateFromDisk = date(int(year), int(month), int(day))

def setStartDate():
    system("clear")

    print("Enter date using only numbers:")
    saveYear = input("Year: ")
    saveMonth = input("Month: ")
    saveDay = input("Day: ")
    
    # I know theres probably a better way to check for this but whatever it works
    try:
        if int(saveDay) < 1 or int(saveDay) > 31 or int(saveMonth) < 1 or int(saveMonth) > 12 or int(saveYear) < 1 or int(saveYear) > 9999:
            continuePrompt("Impossible date. Press ENTER to continue...")
            return
    except Exception:
        continuePrompt("Dates must be stored as numbers with no letters, symbols, or spaces!\n\nPress ENTER to continue...")
        return

    with open(f"/home/{userName}/.local/share/daycounter/date", "w") as storeDate:
        storeDate.write(saveYear + '\n')
        storeDate.write(saveMonth + '\n')
        storeDate.write(saveDay + '\n')
    
    global startDateFromDisk
    startDateFromDisk = date(int(saveYear), int(saveMonth), int(saveDay))

def showDifference():
    global startDateFromDisk
    startDate = startDateFromDisk
    today = date(currentYear, currentMonth, currentDay)
    delta = today - startDate
    print(f"Days passed since {startDate}: {delta.days}\n")

def main():
    if exists(f"/home/{userName}/.local/share/daycounter/date") == True:
        getDateFromDisk()
    else:
        makedirs(f"/home/{userName}/.local/share/daycounter")
        while startDateFromDisk == None:
            setStartDate()
    while True:
        system("clear")
        print(mainMenu)
        showDifference()
        userChoice = input(">")
        if userChoice == "1":
            setStartDate()
        elif userChoice == "2":
            system("clear")
            userIsSure = input("Are you sure you want to quit? Y or N: ")
            if userIsSure == "Y" or userIsSure == "y":
                exit(0)
        else:
            input("Not a valid input! Press ENTER to continue")

if __name__ == "__main__":
    main()
