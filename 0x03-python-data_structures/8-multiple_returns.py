#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        a = ""
        b = None
        return a, b
    else:
        a = len(sentence)
        b = sentence[0]
        return a, b
