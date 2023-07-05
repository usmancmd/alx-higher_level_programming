#!/usr/bin/python3
"""
Sends a request to the URL
displays the body of the response (decoded in utf-8)
"""

import sys
import urllib

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('UTF-8'))
    except urllib.error.HTTPError as err:
        print('Error code:', err.code)
