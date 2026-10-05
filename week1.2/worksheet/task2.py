# Worksheet 1.2: Task 2 Solution
from util import read_numbers
import sys

try:
    numbers = read_numbers()

    numbers.sort()
    #print(numbers)

    min = numbers[0]
    max = numbers[len(numbers)-1]
    mean = sum(numbers) / len(numbers)

    if len(numbers) % 2 == 0:
        mid_index = int(len(numbers) / 2)
        med = numbers[mid_index] - 0.5

    else:
        mid_index = int((len(numbers) / 2) - 0.5)
        med = numbers[mid_index]

    print(f"Minimum = {min}\nMaximum = {max}\nMean = {mean}\nMedian = {med}")

except:
    sys.exit("Error: no numbers provided")
    