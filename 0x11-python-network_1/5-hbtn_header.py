#!/usr/bin/python3
'''
A Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
This should be implemented using Request
'''
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    # Getting the value of the X-Request-Id variable in the dict or headers
    request = requests.get(url).headers['X-Request-Id']
    print(request)
