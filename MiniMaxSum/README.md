# Mini-Max Sum

This algorithm receives an array of 5 positive integers and calculates the minimum and maximum values that can be obtained by summing exactly 4 of the 5 integers.

### Function signature

``` python
def miniMaxSum(arr: List[int]) -> None:
```

## Input

An array of 5 positive integers.

## Output

Prints the minimum and maximum values that can be obtained by summing exactly 4 of the 5 integers.

## Edge Cases

The following are the edge cases for this algorithm:

1. Empty array: If the input array is empty, the algorithm will print an error message and return.
2. Array with less than 5 elements: If the input array has less than 5 elements, the algorithm will print an error message and return.
3. Array with non-integer elements: If the input array contains non-integer elements, the algorithm will print an error message and return.
   
## Complexity

The time complexity of this algorithm is O(n log n), where n is the length of the input array. This is due to the sorting operation performed on the input array. The space complexity of the algorithm is O(1), as it only requires a constant amount of additional space to store the minimum and maximum sums