#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics"""


import sys


def print_stats(size, status_codes):
    """Function that prints the stats"""
    print("File size: {}".format(size))
    for key in sorted(status_codes.keys()):
        if status_codes[key] != 0:
            print("{}: {}".format(key, status_codes[key]))


def parse_line(line):
    """Parse a line of log input and return status code and file size"""
    try:
        parts = line.split()
        if len(parts) < 7:
            return None, None
        
        # Check format: "<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>"
        if parts[-2].isdigit() and parts[-1].isdigit():
            status_code = parts[-2]
            file_size = int(parts[-1])
            return status_code, file_size
        return None, None
    except:
        return None, None


if __name__ == "__main__":
    total_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                   "403": 0, "404": 0, "405": 0, "500": 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            status_code, file_size = parse_line(line)
            
            if file_size is not None:
                total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise
    print_stats(total_size, status_codes)
