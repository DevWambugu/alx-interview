#!/usr/bin/python3
'''0-stats'''
import sys

'''Instatiate variables'''
total_size = 0
status_codes_d = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

l_count = 0

try:
    for line in sys.stdin:
        l_count += 1
        '''This code ignores invalid lines and
        executes the valid ones'''
        try:
            ip, _, _, status_code, file_size = line.split(maxsplit=4)
            status_code = int(status_code)
            file_size = int(file_size)
            total_size += file_size
            status_codes_d[status_code] += 1
        except ValueError:
            pass
        if l_count % 10 == 0:
            print("File size:", total_size)
            for code in sorted(status_codes_d):
                if status_codes_d[code] > 0:
                    print(f"{code}: {status_codes_d[code]}")
            print("-" * 20)
except KeyboardInterrupt:
    pass

'''This code prints the final stats
before it exists'''
for code in sorted(status_codes_d):
    if status_codes_d[code] > 0:
        print(f"{code}: {status_codes_d[code]}")
