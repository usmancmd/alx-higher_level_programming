#!/usr/bin/python3
"""
Takes in a URL and an email address
sends a POST request to the passed URL
with the email as a parameter
finally displays the body of the response.
"""
import requests
import sys

if __name__ == "__main__":
    req = requests.post(sys.argv[1], data={'email': '{}'.format(sys.argv[2])})
    print(req.text)


