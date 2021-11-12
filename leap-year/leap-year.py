# https://medium.com/jungletronics/is-this-leap-year-python-calendar-3d1a61f2c4a7

current_year = int(input("Enter the Year: "))
month = int(input("Enter the Month: "))

print(f"Year: {current_year}")
print(f"Month: {month}")

if (current_year % 4) == 0 and (current_year % 100) != 0 or (current_year % 400) == 0:
    print("\tLeap (bissextile) Year")
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        print("\tThere are 31 days in this month")
    elif month == 4 or month == 6 or month == 9 or month == 11:
        print("\tThere are 30 days in this month")
    elif month == 2:
        print("\tThere are 29 days in this month")
    else:
        print("\tInvalid Mouth")
elif (current_year % 4) != 0 or (current_year % 100) != 0 or (current_year % 400) != 0:
    print("\tNon Leap (common) Year")
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        print("\tThere are 31 days in this month")
    elif month == 4 or month == 6 or month == 9 or month == 11:
        print("\tThere are 30 days in this month")
    elif month == 2:
        print("\tThere are 28 days in this month")
    else:
        print("\tInvalid Mouth")
else:
    print("\tInvalid Year")
