#!/usr/bin/python3
"""
contains a script that reads stdin for a formatted string
and print in aspects prescribed format
"""


import sys
import signal


def printOutput() -> None:
    """
    print the total file size and the status codes in ascending order
    """

    if total_file_size < 1:
        return

    print("File size: ", total_file_size)

    for key, value in codes_dict.items():
        if value != 0:
            print(f"{key}: {str(value)}")

    initCodesDict()


def initCodesDict() -> None:
    """
    set the status code counts to 0 in codes_dict
    """
    global codes_dict
    codes_dict = {"200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0}


codes_dict = None
trimmed_line = None
number_of_lines = 0
status_codes = []
total_file_size = 0

initCodesDict()

try:
    for line in sys.stdin:
        trimmed_line = line.strip()
        trimmed_list = trimmed_line.split(" ")

        list_len = len(trimmed_list)

        if list_len > 2:
            number_of_lines += 1

            if number_of_lines <= 10:
                file_size = trimmed_list[-1]
                status_code = trimmed_list[-2]

                codes_dict[status_code] += 1
                total_file_size += int(file_size)

            if number_of_lines == 10:
                printOutput()
                total_file_size = 0
                status_codes = []
                number_of_lines = 0

finally:
    printOutput()

