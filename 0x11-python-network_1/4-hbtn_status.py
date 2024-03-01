#!/usr/bin/python3
'''
A Python script that fetches https://alx-intranet.hbtn.io/status
This uses the Request'''
import requests

url = "https://alx-intranet.hbtn.io/status"
request = requests.get(url)
content = request.text
# Getting the type of content
print(f'Body response:\n\t- type: {type(content)}')

# Getting the content of data
print(f'\t- content: {content}')
