# Task 2
# Output questions “What is your name?“,
# “How old are you?“,
# Where do you live?“.
# Read the answer of user and output next information:
# “Hello, (answer(name))“,
# “Your age is (answer(age))“,
# “You live in (answer(city))“

name = input("What is your name? ")
age = input("How old are you? ")
city = input("Where do you live? ")

print(f"\"Hello, {name}\",", end=" ")
print(f"\"Your age is {age}\",", end=" ")
print(f"\"You live in, {city}\",")
