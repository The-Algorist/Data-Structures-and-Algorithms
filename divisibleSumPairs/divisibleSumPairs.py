#Given an array of integers and a positive  k , determine the number of  (i,j) pairs where(i<j)  and ar[i] + ar[j] is divisible by k .

# Example
# ar = [1,2,3,4,5,6]
# k=5

# Three pairs meet the criteria:[1,4], [2,3]  and [4,6] .

#code function

import math
import os
import random
import re
import sys

#function
def divisible_sum_pairs(n, k, ar):
    # Edge case: empty array
    if n == 0:
        return 0
    
    # Edge case: small input array
    if n < 2:
        return 0
    
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            # Check if (a[i] + a[j]) is divisible by k
            if (ar[i] + ar[j]) % k == 0:
                count += 1
    
    # Edge case: no pairs satisfy the condition
    if count == 0:
        return 0
    
    # Edge case: all pairs satisfy the condition
    if count == n*(n-1)/2:
        return count
    
    # Edge case: k = 1
    if k == 1:
        return int(n*(n-1)/2)
    
    return count


# if __name__ = '__main__' block here
#   first_multiple_input = input().rstrip().split()

    #n = int(first_multiple_input[0])

    #k = int(first_multiple_input[1])

    #ar = list(map(int, input().rstrip().split()))

    #result = divisibleSumPairs(n, k, ar)