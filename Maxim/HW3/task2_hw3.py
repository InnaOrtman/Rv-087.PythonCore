#!/usr/bin/env python3
# Task 2
# Implement a calculator that translates the amount of information
#   entered by the user in bytes into kilobytes and megabytes

import sys
import os


PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(
    os.path.join(os.getcwd(), os.path.expanduser(__file__))))

sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from mynum import is_number

bytes_ = input("Enter the quantity of bytes: ")

if not is_number(bytes_):
    print("You enter not a number!")
else:
    kbytes = float(bytes_) / 1024
    mbytes = kbytes / 1024
    print(f"{bytes_} B = "
          f"{kbytes} KB = "
          f"{mbytes} MB"
          )
