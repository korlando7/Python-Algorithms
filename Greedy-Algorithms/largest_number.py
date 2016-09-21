#Uses python3

import sys
import random

def largest_number(a):
    #write your code here
    res = ""
    a = sorted([int(x) for x in a], reverse=True)
    k = [str(y) for y in a]
    for num in k:
    	res+= num
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
