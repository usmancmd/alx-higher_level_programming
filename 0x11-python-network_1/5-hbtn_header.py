#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id
in the response header
"""

import requests
import sys

if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    header = req.headers
    for k, v in header.items():
        if k == 'X-Request-Id':
            print(v)

