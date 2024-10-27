#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
- Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
- After every 10 lines and/or keyboard interruption, print statistics
"""

import sys
import re
from typing import Dict, List


def print_statistics(total_size: int, status_codes: Dict[int, int]) -> None:
    """
    Print the computed statistics.
    
    Args:
        total_size (int): Total file size
        status_codes (dict): Dictionary containing status code counts
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def parse_line(line: str) -> tuple:
    """
    Parse a log line and extract status code and file size.
    
    Args:
        line (str): Log line to parse
    
    Returns:
        tuple: (status_code, file_size) or (None, None) if invalid format
    """
    pattern = r'^\S+ - \[.+\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$'
    match = re.match(pattern, line.strip())
    
    if match:
        try:
            status_code = int(match.group(1))
            file_size = int(match.group(2))
            return status_code, file_size
        except ValueError:
            return None, None
    return None, None


def main():
    """Main function to process log lines and compute statistics."""
    total_size = 0
    line_count = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
    }
    
    try:
        for line in sys.stdin:
            status_code, file_size = parse_line(line)
            
            if file_size is not None:
                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1
                    
            line_count += 1
            if line_count % 10 == 0:
                print_statistics(total_size, status_codes)
                
    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)
        raise
    
    
if __name__ == "__main__":
    main()#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
- Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
- After every 10 lines and/or keyboard interruption, print statistics
"""

import sys
import re
from typing import Dict, List


def print_statistics(total_size: int, status_codes: Dict[int, int]) -> None:
    """
    Print the computed statistics.
    
    Args:
        total_size (int): Total file size
        status_codes (dict): Dictionary containing status code counts
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def parse_line(line: str) -> tuple:
    """
    Parse a log line and extract status code and file size.
    
    Args:
        line (str): Log line to parse
    
    Returns:
        tuple: (status_code, file_size) or (None, None) if invalid format
    """
    pattern = r'^\S+ - \[.+\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$'
    match = re.match(pattern, line.strip())
    
    if match:
        try:
            status_code = int(match.group(1))
            file_size = int(match.group(2))
            return status_code, file_size
        except ValueError:
            return None, None
    return None, None


def main():
    """Main function to process log lines and compute statistics."""
    total_size = 0
    line_count = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
    }
    
    try:
        for line in sys.stdin:
            status_code, file_size = parse_line(line)
            
            if file_size is not None:
                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1
                    
            line_count += 1
            if line_count % 10 == 0:
                print_statistics(total_size, status_codes)
                
    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)
        raise
    
    
if __name__ == "__main__":
    main()
