year = int(input("Please input year.\n"))

if year <= 0:
    year = int(input("Year can't be zero or negative, please input again.\n"))

if year % 400 == 0:
    print(f"Year {year} is intercalary")
elif year % 4 == 0 and year % 100 != 0:
    print(f"Year {year} in intercalary")
else:
    print(f"Year {year} is not intercalary")

century = year/100 if year%100 == 0 else year/100 + 1

print(f"Year {year} belongs to {int(century)} century")