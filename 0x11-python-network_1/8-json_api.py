#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]
    data = {'q': letter}

    req = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        res = req.json()
        if res == {}:
            print('No result')
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print('Not a valid JSON')
