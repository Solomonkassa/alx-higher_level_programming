#!/usr/bin/python3
"""api thing"""
import sys
import requests


def apidata():
    """apidata"""
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2],
                                                              sys.argv[1])
    result = requests.get(url)
    try:
        d = result.json()
        for i in range(10):
            print("{}: {}".format(d[i]["sha"],
                                  d[i]["commit"]["author"]["name"]))
    except IndexError:
        pass

if __name__ == "__main__":
    apidata()
