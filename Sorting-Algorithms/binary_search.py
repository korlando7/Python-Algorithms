# Uses python3
import random

def binary_search(a, key):
    print (a)
    low = 0
    high = len(a)-1
    while low <= high:
        mid = low + (high-low)//2
        if a[mid] == key:
            return mid, key
        else:
            if key < a[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return False