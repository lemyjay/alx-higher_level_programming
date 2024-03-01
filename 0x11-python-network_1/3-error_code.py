#!/usr/bin/python3
'''
A Python script that takes in a URL, sends a request to the
URL and displays the body of the response (decoded in utf-8).
'''
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)

    # Fetching the response
    try:
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError as e:
        # e is of the form 'HTTP Error 404: Not Found'
        # so using split to get the status code part
        # I later on realized I could have just used e.code
        e = str(e)
        e = e.split(' ')
        print("Error code: {}".format(e[2][:3]))
