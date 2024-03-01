#!/usr/bin/python3
'''A Python script that fetches https://alx-intranet.hbtn.io/status'''
import urllib.request

url = "https://alx-intranet.hbtn.io/status"
req = urllib.request.Request(url)

# Fetching the response
with urllib.request.urlopen(req) as response:
    data = response.read()

    # Getting the type of the content (class 'bytes')
    print(f'Body response:\n\t- type: {type(data)}')

    # Getting the content (b'OK')
    print(f'\t- content: {data}')

    # Getting the utf8 content ('OK')
    print(f'\t- utf8 content: {data.decode("utf-8")}')
