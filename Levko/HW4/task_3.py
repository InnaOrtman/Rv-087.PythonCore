# task_3

question = int(input("Enter the number, please: "))

if question > 0:
    print("It`s positive!")
elif question < 0:
    print("It`s negative!")
else:
    print("Zero is neither positive nor negative")

if 0 < question < 10:
    print("It`s one-digit!")
elif question > 10:
    print("It`s two or more digit:)!")

if 0 > question <= -10:
    print("It`s two or more digit:)!")
elif 0 > question > -10:
    print("It`s one-digit!")

