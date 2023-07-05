#!/usr/bin/python3
"""
Sends a request to the URL
displays the value of the X-Request-Id variable
found in the header of the response
"""

import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as res:
        headers = res.getheaders()
        for i in headers:
            if i[0] == 'X-Request-Id':
                print(i[1])
