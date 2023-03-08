## Plus Minus Algorithm

The plusMinus algorithm is a simple function that takes an array of integers as input and prints out the fractions of positive, negative, and zero integers in the array. It does this by iterating over each element of the array and counting the number of positive, negative, and zero integers. It then divides these counts by the length of the array to calculate the fractions, and prints them out to the console.

### Usage

The plusMinus algorithm can be used in any Python program that needs to calculate the fractions of positive, negative, and zero integers in an array. To use the algorithm, you can simply call the plusMinus function and pass in an array of integers as an argument:

```

arr = [1, -2, 0, 3, -1]
plusMinus(arr)
```

This will output:

```

0.400000
0.400000
0.200000
```

### Time and Space Complexity

The time complexity of the plusMinus algorithm is O(n), where n is the length of the input array. This is because the algorithm iterates over each element in the array once, performing a constant number of operations for each element. Therefore, the time taken by the algorithm is proportional to the size of the input array.

The space complexity of the algorithm is O(1), which is constant. This is because the algorithm only uses a fixed number of variables to keep track of the fractions of positive, negative, and zero integers in the array. The space used by the algorithm does not increase with the size of the input array. Therefore, the algorithm is said to be space-efficient.
