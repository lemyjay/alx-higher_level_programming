#!/usr/bin/python3
'''
A Python script that takes in a URL and an email, sends a POST request to the
passed URLwith the email as a parameter, and displays the
body of the response (decoded in utf-8).
'''
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    value = {}
    value['email'] = email
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)

    # Fetching the response
    with urllib.request.urlopen(req) as response:
        content = response.read().decode('utf-8')
        print(content)
