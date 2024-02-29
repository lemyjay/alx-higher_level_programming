#!/usr/bin/python3
'''A function that finds the peak in a given list of integers'''


def find_peak(list_of_integers):
    # Finds the peak in a given list of integers.

    # Check if the list is empty
    if not list_of_integers:
        return None

    arr = list_of_integers
    length = len(arr)
    # Check if the list has only one element
    if length == 1:
        return arr[0]

    # Check if the first element is a peak
    if arr[0] >= arr[1] and length == 2:
        return arr[0]

    # Iterate through the list and check if the current element is a peak
    for i in range(length):
        if i == 0:
            arr[0] >= arr[1]
            return arr[0]
        if arr[i - 1] <= arr[i] and arr[i + 1] <= arr[i]:
            return(arr[i])

    # Check if the last element is a peak
    if arr[-1] >= arr[-2]:
        return arr[-1]
    elif arr[0] >= arr[1]:
        return arr[0]

    # If no peak is found, return None
    return None
