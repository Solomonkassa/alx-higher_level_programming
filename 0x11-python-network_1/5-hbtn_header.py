#!/usr/bin/python3
"""Check status"""
import requests
import sys


def header():
    """status"""
    result = requests.get(sys.argv[1])

    print(result.headers.get("X-Request-Id", None))

if __name__ == "__main__":
    header()
