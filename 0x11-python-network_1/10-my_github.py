#!/usr/bin/python3
"""Write a Python script that fetches https://alx-intranet.hbtn.io/status
You must use the package urllib"""


if __name__ == "__main__":
    import requests
    from sys import argv
    import json

    username = argv[1]
    token = argv[2]
    headers = {'Authorization': 'token ' + token}
    login = requests.get('https://api.github.com/\
                         search/repositories?q=github+api',
                         auth=(username, token))

    if 'application/json' in login.headers.get('Content-Type', ''):
        res = login.json()
            print("{}".format(login.json().get('id')))
    else:
        print('Not a valid JSON')
