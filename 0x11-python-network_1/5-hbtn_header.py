#!/usr/bin/python3
""""Write a Python script that takes in a URL, sends a
0request to the URL and displays the value of the
X-Request-Id variable found in the header of the response."""


if __name__ == "__main__":
    import requests
    from sys import argv

    res = requests.get(argv[1])
    print(dict(res.headers).get("X-Request-Id"))
