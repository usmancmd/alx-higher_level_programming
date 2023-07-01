#!/bin/bash
# Sends a DELETE request to the URL
# Passed as the first argument and displays the body of the response

curl -sX DELETE "$1"
