#!/usr/bin/python3
"""Check status"""
import requests
import sys


def post():
    """status"""
    result = requests.post(sys.argv[1], data={"email": sys.argv[2]})

    print(result.text)

if __name__ == "__main__":
    post()
