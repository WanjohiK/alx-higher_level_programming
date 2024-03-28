#!/usr/bin/python3
"""
script that Lists 10 commits in a repo
"""

if __name__ == '__main__':
    import sys
    import requests

    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        sys.argv[2], sys.argv[1])
    try:
        res = requests.get(url)
        res_dict = res.json()
        for i in range(0, 10):
            print("{}: {}".format(res_dict[i].get('sha'), res_dict[i].get(
                'commit').get('author').get('name')))
    except Exception:
        pass
