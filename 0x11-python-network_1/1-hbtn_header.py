#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header of the response.
"""


if __name__ == "__main__":
    import sys
    import urllib.request
    req = sys.argv[1]
    with urllib.request.urlopen(req) as response:
        body = response.info()
        print(body['X-Request-Id'])
