#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Task 2
# Output questions “What is your name?“,
# “How old are you?“,
# Where do you live?“.
# Read the answer of user and output next information:
# “Hello, (answer(name))“,
# “Your age is (answer(age))“,
# “You live in (answer(city))“

name = raw_input("What is your name? ")
age = raw_input("How old are you? ")
city = raw_input("Where do you live? ")

print u"\"Hello, {}\" ".format(name),
print u"\"Your age is {}\" ".format(age),
print u"\"You live in {}\"".format(city)


