# lazy functionality don't execute all the operations only the requesteds

# Seq 1 to 9,000,000

import sys

def mygenerator(n):
    for x in range(n):
        yield x ** 3

values = mygenerator(90000000)

# print(sys.getsizeof(values))


# Generate Infinite sequences

def infinite_sequence():
    result = 1
    while True:
        yield result
        result *= 5

values = infinite_sequence()