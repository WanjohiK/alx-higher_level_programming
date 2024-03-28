#!/usr/bin/python3
"""
script that takes GitHub credentials (username and password)
as arguments
and uses the GitHub API to display users id
"""


if __name__ == '__main__':
    import sys
    import requests

    url = "https://api.github.com/user"
    res = requests.get(
        url, auth=requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    res_dict = res.json()
    print(res_dict.get('id'))
