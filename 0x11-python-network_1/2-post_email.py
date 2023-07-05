#!/usr/bin/python3
"""
Takes in a URL and an email
and sends a POST request to the passed URL
with the email as a parameter
displays the body of the response (decoded in utf-8)
"""

import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    data = {"email": sys.argv[2]}
    value = urllib.parse.urlencode(data).encode("ascii")

    req = urllib.request.Request(sys.argv[1], value)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode("utf-8"))
