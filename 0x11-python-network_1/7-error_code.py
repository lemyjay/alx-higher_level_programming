#!/usr/bin/python3
'''
A Python script that takes in a URL, sends a request to the
URL and displays the body of the response (decoded in utf-8).
'''
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    # Fetching the response
    request = requests.get(url)
    stat_code = request.status_code
    if stat_code >= 400:
        print('Error code: {}'.format(stat_code))
    else:
        print(request.text)
