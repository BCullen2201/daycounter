from os import system
from sys import exit
from datetime import date

today = date.today()
month = int(today.strftime("%m"))
day = int(today.strftime("%d"))
year = int(today.strftime("%Y"))

def main():
    system("clear")
    startDate = date(1964, 8, 14)
    today = date(year, month, day)
    delta = today - startDate
    print(f"Days passed since {startDate}: {delta.days}")

if __name__ == "__main__":
    main()