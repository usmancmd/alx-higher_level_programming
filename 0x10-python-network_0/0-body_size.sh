#!/usr/bin/env bash
# Sends a request to that URL
# And displays the size of the body of the response

curl -s "$1" | wc -c
