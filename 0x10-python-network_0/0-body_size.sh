#!/bin/bash
# takes in a URL, sends a request to that URL, displays the size of the body of the response
curl -sI GET "$1" | grep -i "Content-Length" | cut -d " " -f2
