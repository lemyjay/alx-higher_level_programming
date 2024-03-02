#!/usr/bin/python3
'''
A Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the
body of the response.
'''
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    value = {}
    value['email'] = email
    # data = urllib.parse.urlencode(value)
    # data = data.encode('ascii')
    request = requests.get(url, value)
    print(request.text)
