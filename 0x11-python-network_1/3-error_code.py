#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""


if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.error
    req = sys.argv[1]
    urllib.request.Request(req)
    try:
        with urllib.request.urlopen(req) as response:
            req = response.read()
            print(req.decode("utf-8"))

    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
