#!/usr/bin/python3
"""Write a Python script that fetches https://alx-intranet.hbtn.io/status
You must use the package urllib"""


if __name__ == "__main__":
    import requests
    from sys import argv
    import json

    headers = {'Authorization': 'token ' + token}

    login = requests.get('https://api.github.com/user', headers=headers)

    if 'application/json' in login.headers.get('Content-Type', ''):
        res = login.json()
        if res != {}:
            print("{}".format(res.get('id')))
        else:
            print('No result')
    else:
        print('Not a valid JSON')
