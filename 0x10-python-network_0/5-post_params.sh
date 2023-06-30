#!/bin/bash
# takes in a URL, sends a POST request to the passed URL, displays the body of the response
curl "$1" -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
