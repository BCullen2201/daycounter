#!/usr/bin/env python3

from os import system
from sys import exit
from datetime import date
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

def continuePrompt(continuePromptMsg):
    input(f"\n{continuePromptMsg}")

def setStartDate():
    system("clear")
    saveYear = input("Year: ")
    saveMonth = input("Month: ")
    saveDay = input("Day: ")
    
    try:
        if int(saveDay) < 1 or int(saveDay) > 31 or int(saveMonth) < 1 or int(saveMonth) > 12 or int(saveYear) < 1 or int(saveYear) > 9999:
            continuePrompt("Impossible date. Press ENTER to continue...")
            return
    except Exception:
        continuePrompt("Dates must be stored as numbers, not words! (Example: 2023-6-22)\n\nPress ENTER to continue...")
        return

    with open(f"/home/{userName}/.day-counter/date.txt", "w") as storeDate:
        storeDate.write(saveYear + '\n')
        storeDate.write(saveMonth + '\n')
        storeDate.write(saveDay + '\n')

def showDifference():
    try:
        getDate = open(f"/home/{userName}/.day-counter/date.txt", "r")
    except Exception:
        print("Please enter a start date!")
        return

    year = getDate.readline().rstrip()
    month = getDate.readline().rstrip()
    day = getDate.readline().rstrip()

    startDate = date(int(year), int(month), int(day))
    today = date(currentYear, currentMonth, currentDay)
    delta = today - startDate
    print(f"Days passed since {startDate}: {delta.days}\n")

    getDate.close()

def main():
    while True:
        system("clear")
        print(f"{mainMenu}")
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
