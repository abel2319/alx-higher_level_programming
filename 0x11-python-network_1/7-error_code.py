#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to
the URL and displays the body of the response (decoded in utf-8)."""


if __name__ == "__main__":
    from sys import argv
    from requests

    req = requests(argv[1])
    try:
        req = requests(argv[1])
        print(req.text)
    except:
        print('Error code: {}'.format(req.status_code))
