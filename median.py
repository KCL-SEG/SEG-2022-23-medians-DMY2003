"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from math import floor

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)

numbers.sort()

if len(numbers) % 2 == 0:
    print(numbers[int(len(numbers)/2-1)])
    print(numbers[int(len(numbers)/2)])
else:
    print(numbers[floor(len(numbers)/2)])