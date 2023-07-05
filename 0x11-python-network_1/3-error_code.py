#!/usr/bin/python3
"""
Sends a request to the URL
displays the body of the response (decoded in utf-8)
"""

import sys
import urllib

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[2]) as res:
            print(res.read().decode('UTF-8'))
    except urllib.error.HTTPError as err:
        print('Error code:', err.code)
