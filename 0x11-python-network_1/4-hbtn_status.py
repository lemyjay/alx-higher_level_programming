#!/usr/bin/python3
'''A Python script that fetches https://alx-intranet.hbtn.io/status'''
import urllib.request

url = "https://alx-intranet.hbtn.io/status"
req = urllib.request.Request(url)

if __name__ == '__main__':
    # Fetching the response
    with urllib.request.urlopen(req) as response:
        data = response.read().decode("utf-8")

        # Getting the type of data
        print(f'Body response:\n\t- type: {type(data)}')

        # Getting the content of data
        print(f'\t- content: {data}')
