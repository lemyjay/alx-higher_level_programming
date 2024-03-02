#!/usr/bin/python3
'''
A Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter as a parameter.

The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty,
display the id and name like this: [<id>] <name>
Otherwise:
    - Display Not a valid JSON if the JSON is invalid
    - Display No result if the JSON is empty
The package requests and sys must be used.
'''
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ''
    else:
        q = sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"
    values = {}
    values['q'] = q

    # Fetching the response
    request = requests.post(url, values)
    if request.json and len(request.json) != 0:
        name = request.json['name']
        id = request.json['id']
        print('[{}] {}'.format(id, name))
    elif not request.json:
        print('Not a valid JSON')
    elif len(request.json) == 0:
        print('No result')
