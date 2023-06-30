#!/usr/bin/python3
"""Check status"""
import requests


def status():
    """status"""
    result = requests.get("https://intranet.hbtn.io/status")

    print("Body response:")
    print("\t- type: {}".format(type(result.text)))
    print("\t- content: {}".format(result.text))

if __name__ == "__main__":
    status()
