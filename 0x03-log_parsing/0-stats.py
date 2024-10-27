#!/usr/bin/python3
"""
log parsing
"""
import sys
import re


def output(log: dict) -> None:
    """
    helper function to display stats
    """
    print("File size: {}".format(log["file_size"]))
    for code in sorted(log["code_frequency"]):
        if log["code_frequency"][code]:
            print("{}: {}".format(code, log["code_frequency"][code]))


if __name__ == "__main__":
    regex = re.compile(
        r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - '
        r'\[(.*?)\] "GET /projects/260 HTTP/1.1" '
        r'(\d{3}) (\d+)$'
    )

    line_count = 0
    log = {}
    log["file_size"] = 0
    log["code_frequency"] = {
        str(code): 0 for code in [
            200, 301, 400, 401, 403, 404, 405, 500]}

    try:
        for line in sys.stdin:
            line = line.strip()
            match = regex.match(line)
            if match:
                line_count += 1
                code = match.group(3)  # Changed from group(1) to group(3)
                file_size = int(match.group(4))  # Changed from group(2) to group(4)
                
                # File size
                log["file_size"] += file_size
                
                # status code
                if code in log["code_frequency"]:
                    log["code_frequency"][code] += 1
                    
                if line_count % 10 == 0:
                    output(log)
    except KeyboardInterrupt:
        output(log)
        raise
    finally:
        output(log)
