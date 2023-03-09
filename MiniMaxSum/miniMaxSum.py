# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.


import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Edge case: empty array
    if not arr:
        print("Error: Empty array")
        return
    
    # Edge case: array with less than 5 elements
    if len(arr) < 5:
        print("Error: Array should have at least 5 elements")
        return
    
    # Edge case: array with non-integer elements
    if not all(isinstance(i, int) for i in arr):
        print("Error: Array should contain only integers")
        return
    
    arr.sort()
    min_sum = sum(arr[:4])
    max_sum = sum(arr[-4:])
    print(min_sum, max_sum)
