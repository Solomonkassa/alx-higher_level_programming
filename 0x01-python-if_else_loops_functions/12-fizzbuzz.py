#!/usr/bin/python3
def fizzbuzz():
  for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
      n = "fizzbuzz"
    elif n % 3 == 0:
      n = "fizz"
    elif n % 5 == 0:
      n = "buzz"
    print ("{}".format(n), end=" ")
