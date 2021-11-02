# Task 1
# The YEAR is known. Determine whether this year is intercalary and to what century this year belongs
# Year известен. Определите, является ли этот Year высокосным и к какому веку принадлежит этот Year.
		# 	Year високосный, если он делится на четыре без остатка, но если он делится на 100 без остатка, это не Leap year.
		# 	Однако, если он делится без остатка на 400, это Leap year. Таким образом, 2000 г. является особым високосным Yearом,
		# 	который бывает лишь раз в 400 лет.

year = int(input('Input YEAR: '))
#age = int("%.0f" % (year / 100)) +1
age = (year // 100) +1
leap_year = year % 4
leap400 = year % 400
leap100 = year % 100

print(age, 'century')

if leap400 == 0:
	print("Year ", year, " - Leap year ")

elif ((leap_year == 0) and (leap100 != 0)):
	print("Year ", year, " - Leap year ")

elif ((leap100 == 0) and (leap400 != 0)): 
 	print("Year ", year, " - normal")

else:
    print("Year ", year, " - normal")