#!/usr/bin/python3
"""
script that takes in a URL and an email,
sends a POST request to the passed URL
with the email as a parameter, and
displays the body of the response (decoded in utf-8)
"""


if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse
    url = sys.argv[1]
    myemail = {'email': sys.argv[2]}
    email = urllib.parse.urlencode(myemail)
    email = email.encode('ascii')
    req = urllib.request.Request(url, email)

    with urllib.request.urlopen(req) as response:
        res = response.read()
        body = res.decode('utf-8')
        print(body)
