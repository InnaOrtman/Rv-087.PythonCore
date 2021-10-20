# Task 1 (Python 3)
# Define variables a and b. Read values a and b from console and calculate:
#     a + b
#     a - b
#     a * b
#     a / b.
# Output obtained results.

def is_number(variable: str) -> bool:
    count_dot = 0
    for i in range(len(variable)):
        if count_dot > 1:
            return False
        if variable[i] == ".":
            count_dot += 1
            continue
        try:
            int(variable[i])
        except ValueError:
            return False
    return True


def if_int_to_int(number: [int, float]) -> [int, float]:
    if number % 1 == 0:
        return int(number)
    return number


def main():
    a = input("Enter value of variable a: ")
    b = input("Enter value of variable b: ")

    if is_number(a) and is_number(b):
        a = float(a)
        b = float(b)
        print(f"a + b = {if_int_to_int(a + b)}")
        print(f"a - b = {if_int_to_int(a - b)}")
        print(f"a * b = {if_int_to_int(a * b)}")

        try:
            truediv = a / b
        except ZeroDivisionError:
            truediv = f"{a} / {b}: You can't division on 0"
        if not is_number(str(truediv)):
            print(truediv)
        else:
            print(f"a / b = {if_int_to_int(truediv)}")
    else:
        print("Variable a or b not is a number (a = {}, b = {})".format(a, b))


if __name__ == "__main__":
    main()
