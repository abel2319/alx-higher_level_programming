#!/usr/bin/python3
"""Write a Python script that fetches https://alx-intranet.hbtn.io/status
You must use the package urllib"""


if __name__ == "__main__":
    import urllib.request
    from sys import argv
    with urllib.request.urlopen(argv[1]) as response:
        print(dict(response.headers).get("X-Request-Id"))
