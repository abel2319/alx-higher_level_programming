#!/usr/bin/python3
"""Write a Python script that fetches https://alx-intranet.hbtn.io/status
You must use the package urllib"""


if __name__ == "__main__":
    import requests
    from sys import argv
    import json

    q = ""
    if len(argv) > 1:
        q = argv[1]

    response = requests.post('http://0.0.0.0:5000/search_user',
                             data={'q': q})
    if 'application/json' in response.headers.get('Content-Type', ''):
        res = response.json()
        if res is not None:
            print("[{}] {}".format(res['id'], res['name']))
        else:
            print('No result')
    else:
        print('Not a valide JSON')
