from datetime import datetime

def main():
    now=datetime.now()

    # %y/%Y for year, %b/%B for month,  %a/%A for weekend, %d for date
    print(now.strftime("The current year: %Y"))
    print(now.strftime("%A, %d , %B, %Y"))

    # %c for Locale date and time, %x for Locale date, %X Locale time
    print(now.strftime("Locale date and time:%c"))
    print(now.strftime("Locale date:%x"))
    print(now.strftime("Locale time:%X"))

    ### TIME FORMATTING ###

    # %I/%H - 12/24 hour, %M - minutes %S - second, %p - locale's AM/PM
    print(now.strftime("The current time : %I:%M:%S %p"))
    print(now.strftime("24-hour time : %H:%M"))

if __name__ == "__main__":
      main()