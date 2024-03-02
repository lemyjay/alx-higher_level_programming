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
    response = requests.post(url, values)
    try:
        json_data = response.json()

        if json_data:
            name = json_data.get('name')
            id = json_data.get('id')
            print('[{}] {}'.format(id, name))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
