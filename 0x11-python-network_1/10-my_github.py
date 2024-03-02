#!/usr/bin/python3
'''
A Python script that takes my GitHub credentials (username and password)
and uses the GitHub API to display your id.
'''
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]
    
    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, passwd))

    try:
        json_data = response.json()

        if json_data.get('id'):
            print(json_data.get('id'))
        else:
            print("None")
    except ValueError:
        print("None")
