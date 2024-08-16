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

    for key in sorted(codes_dict.keys()):
        value = codes_dict[key]
        if value != 0:
            print(f"{key}: {value}")


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
number_of_lines = 0
total_file_size = 0
line_process_ends = False
pattern = (
    r'(\d{1,3}(?:\.\d{1,3}){3}) - \[(.*?)\] '
    r'"GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'
)

try:
    for line in sys.stdin:
        line_process_ends = False
        match = re.match(pattern, line.strip())

        if match:
            try:
                file_size = int(match.group(4))
                status_code = match.group(3)
                total_file_size += file_size

                if status_code in codes_dict.keys():
                    codes_dict[status_code] += 1
                number_of_lines += 1

                if number_of_lines == 10:
                    print_output()
                    number_of_lines = 0
            except ValueError:
                continue
        line_process_ends = True

finally:
    if not line_process_ends and number_of_lines != 10:
        print_output()
