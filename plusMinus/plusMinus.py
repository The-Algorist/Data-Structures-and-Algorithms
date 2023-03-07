# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10^-4 are acceptable

import math
import os
import random
import re
import sys

def plusMinus(arr):
    n = len(arr)
    if n == 0:
        # handle the case of an empty array
        print("{:.6f}".format(0))
        print("{:.6f}".format(0))
        print("{:.6f}".format(0))
        return

    # initialize the variables positive, negative and zero
    positive=negative=zero=0

    #iterate through the array
    for i in arr:
        if i>0:
            positive += 1
        elif i<0:
            negative += 1
        else:
            zero += 1

    if positive == 0:
        # handle the case of an array with all negative or zero integers
        print("{:.6f}".format(0))
        print("{:.6f}".format(negative/n))
        print("{:.6f}".format(zero/n))
        return

    if negative == 0:
        # handle the case of an array with all positive or zero integers
        print("{:.6f}".format(positive/n))
        print("{:.6f}".format(0))
        print("{:.6f}".format(zero/n))
        return
    
    if zero == 0:
        # handle the case of an array with all positive or negative integers
        print("{:.6f}".format(positive/n))
        print("{:.6f}".format(negative/n))
        print("{:.6f}".format(0))
        return

    # handle the general case
    print("{:.6f}".format(positive/n))
    print("{:.6f}".format(negative/n))
    print("{:.6f}".format(zero/n))

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)