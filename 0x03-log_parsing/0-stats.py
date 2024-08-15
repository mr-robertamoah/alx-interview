#!/usr/bin/python3

"""
Contains a script that reads stdin for a formatted string
and print in aspects prescribed format.
"""

import sys
import re


def print_output():
    """
    Print the total file size and the status codes in ascending order.
    """

    if total_file_size < 1:
        return

    print(f"File size: {total_file_size}")

    for key, value in codes_dict.items():
        if value != 0:
            print(f"{key}: {str(value)}")


def init_codes_dict():
    """
    Set the status code counts to 0 in codes_dict.
    """
    return {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }


codes_dict = init_codes_dict()
trimmed_line = None
number_of_lines = 0
total_file_size = 0
pattern = (
    r'(\d{1,3}(?:\.\d{1,3}){3}) - \[(.*?)\] '
    r'"GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'
)

try:
    for line in sys.stdin:
        trimmed_line = line.strip()
        match = re.match(pattern, trimmed_line)

        if match:
            number_of_lines += 1

            if number_of_lines <= 10:
                file_size = match.group(4)
                status_code = match.group(3)
                codes_dict[status_code] += 1
                total_file_size += int(file_size)

            if number_of_lines == 10:
                print_output()
                total_file_size = 0
                status_codes = []
                number_of_lines = 0
                codes_dict = init_codes_dict()

finally:
    print_output()
