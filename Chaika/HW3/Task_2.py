# Задача 2
# Реализовать калькулятор, который переводит количество информации, введенной пользователем в байтах, в килобайты и мегабайты.
print("Task 2")
byte = int(input("input bytes: "))
kilobyte = (byte/1024)
megabyte = (kilobyte/1024)

print(" ")
print(byte, " = bytes" )
print( "%.3f" % kilobyte, " = Kilobytes" )
print( "%.3f" % megabyte, " = Megabytes" ) 