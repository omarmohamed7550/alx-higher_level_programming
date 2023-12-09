#!/usr/bin/python3
def number_keys(a_dictionary):
    numbers = 0
    keys = list(a_dictionary.keys())

    for i in keys:
        numbers += 1

    return (numbers)
