#!/usr/bin/python3
"""Check status"""
import requests
import sys


def searchapi():
    """status"""
    result = requests.get("https://swapi.co/api/people",
                          params={"search": sys.argv[1]})

    try:
        data = result.json()
        print("Number of results: {}".format(data["count"]))
        for i in data["results"]:
            print(i["name"])
    except:
        print("Not a valid JSON")

if __name__ == "__main__":
    searchapi()
