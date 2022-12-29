#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to
the URL and displays the body of the response."""


if __name__ == "__main__":
    from sys import argv
    from requests

    req = requests(argv[1])
    req = requests(argv[1])
    if req.raise_for_status is not None:
        print('Error code: {}'.format(req.status_code))
    else:
        print(req.text)
