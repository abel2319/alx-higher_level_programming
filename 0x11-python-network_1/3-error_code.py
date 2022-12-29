#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to
the URL and displays the body of the response (decoded in utf-8)."""


if __name__ == "__main__":
    from sys import argv
    from urllib.request import Request, urlopen
    from urllib.error import URLError, HTTPError

    req = Request(argv[1])
    try:
        with urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code: ', e.code)
