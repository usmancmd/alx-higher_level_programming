#!/bin/bash
# Sends a request to a URL, displays status code of the response of the URL
curl -s -o /dev/null -w "%{http_code}" "$1"
