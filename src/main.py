from os import system
from sys import exit
from datetime import date

mainMenu = """Day Counter
=======================
1 - Set start date
2 - Show days passed
3 - Exit
=======================
"""

today = date.today()
currentMonth = int(today.strftime("%m"))
currentDay = int(today.strftime("%d"))
currentYear = int(today.strftime("%Y"))

def setStartDate():
    system("clear")
    saveYear = input("Year: ")
    saveMonth = input("Month: ")
    saveDay = input("Day: ")

    with open('../date/year.txt', 'w') as storeYear:
        storeYear.write(saveYear)

    with open('../date/month.txt', 'w') as storeMonth:
        storeMonth.write(saveMonth)

    with open('../date/day.txt', 'w') as storeDay:
        storeDay.write(saveDay)

def showDifference():
    system("clear")
    try:
        getYear = open('../date/year.txt', 'r')
        getMonth = open('../date/month.txt', 'r')
        getDay = open('../date/day.txt', 'r')
    except Exception:
        print("Please enter a start date!")
        input("Press ENTER to continue")
        return

    startDate = date(int(getYear.read()), int(getMonth.read()), int(getDay.read()))
    today = date(currentYear, currentMonth, currentDay)
    delta = today - startDate
    print(f"Days passed since {startDate}: {delta.days}")
    input("Press ENTER to continue")

def main():
    while True:
        system("clear")
        print(mainMenu)
        userChoice = input(">")
        if userChoice == "1":
            setStartDate()
        elif userChoice == "2":
            showDifference()
        elif userChoice == "3":
            userIsSure = input("Are you sure you want to quit? Y or N: ")
            if userIsSure == "Y" or userIsSure == "y":
                exit(0)
            elif userIsSure == "N" or userIsSure == "n":
                return
            else:
                return

if __name__ == "__main__":
    main()