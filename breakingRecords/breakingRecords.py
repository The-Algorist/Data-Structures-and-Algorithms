import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#


from typing import List, Tuple

def breakingRecords(scores: List[int]) -> Tuple[int, int]:
    # Edge case: empty array
    if not scores:
        return (0, 0)
    
    # Edge case: array with less than 2 elements
    if len(scores) < 2:
        return (0, 0)
    
    # Edge case: array with non-integer elements
    if not all(isinstance(i, int) for i in scores):
        raise TypeError("Array should contain only integers")
    
    max_score = min_score = scores[0]
    max_count = min_count = 0
    
    for score in scores[1:]:
        if score > max_score:
            max_score = score
            max_count += 1
        elif score < min_score:
            min_score = score
            min_count += 1
            
    return (max_count, min_count)