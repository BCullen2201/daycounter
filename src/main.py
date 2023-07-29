from os import system
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

def setStartDate():
    system("clear")
    saveYear = input("Year: ")
    saveMonth = input("Month: ")
    saveDay = input("Day: ")

    with open(f'/home/{userName}/.day-counter/year.txt', 'w') as storeYear:
        storeYear.write(saveYear)

    with open(f'/home/{userName}/.day-counter/month.txt', 'w') as storeMonth:
        storeMonth.write(saveMonth)

    with open(f'/home/{userName}/.day-counter/day.txt', 'w') as storeDay:
        storeDay.write(saveDay)

def showDifference():
    try:
        getYear = open(f'/home/{userName}/.day-counter/year.txt', 'r')
        getMonth = open(f'/home/{userName}/.day-counter/month.txt', 'r')
        getDay = open(f'/home/{userName}/.day-counter/day.txt', 'r')
    except Exception:
        print("Please enter a start date!")
        return

    startDate = date(int(getYear.read()), int(getMonth.read()), int(getDay.read()))
    today = date(currentYear, currentMonth, currentDay)
    delta = today - startDate
    print(f"Days passed since {startDate}: {delta.days}\n")

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
            elif userIsSure == "N" or userIsSure == "n":
                return
            else:
                return
        else:
            input("Not a valid input! Press ENTER to continue")
            return

if __name__ == "__main__":
    main()
