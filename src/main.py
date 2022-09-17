from os import system
from sys import exit
from datetime import date

welcomeMessage = """Day Counter

1 - Set start date
2 - Exit
"""

today = date.today()
month = int(today.strftime("%m"))
day = int(today.strftime("%d"))
year = int(today.strftime("%Y"))

def setStartDate():
    print("Enter date correctly, without quotes E.g. '2005, 11, 05'")
    startDate = input(">")

    with open('date.txt', 'w') as saveDate:
        saveDate.write(startDate)

def main():
    system("clear")
    print(welcomeMessage)
    userChoice = input(">")
    if userChoice == "1":
        setStartDate()
    elif userChoice == "2":
        userIsSure = input("Are you sure you want to quit? Y or N: ")
        if userIsSure == "Y" or userIsSure == "y":
            exit(0)
        elif userIsSure == "N" or userIsSure == "n":
            return
        else:
            return
    
    # startDate = date(1964, 8, 14)
    # today = date(year, month, day)
    # delta = today - startDate
    # print(f"Days passed since {startDate}: {delta.days}")

if __name__ == "__main__":
    main()