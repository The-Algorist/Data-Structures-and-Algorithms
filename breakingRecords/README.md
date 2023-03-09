# Breaking Records

## Problem description

Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.

## Function description

Complete the function 'breakingRecords(scores: List[int]) -> Tuple[int, int]' in the editor below.

- breakingRecords has the following parameter(s):

- scores: an array of integers representing scores of each game Maria played.
- 
The function should return a tuple with two elements:

- The first element is an integer representing the number of times Maria broke her record for most points scored in a game.
- The second element is an integer representing the number of times she broke her record for least points scored in a game.
  
Example
Input:

```
9
10 5 20 20 4 5 2 25 1
```

Output:

```
2 4
```

Constraints

1 <= n <= 1000
0 <= scores[i] <= 10^8

## Edge Cases

The following edge cases are handled in the implementation:

- If the input array scores is empty, the function returns (0, 0).
- If the input array scores has less than 2 elements, the function returns (0, 0).
- If the input array scores contains non-integer elements, the function raises a TypeError.
  
## Space and Time Complexity

The time complexity of this function is O(n), where n is the length of the input array. This is because we iterate through the array once.

The space complexity of this function is O(1), because we only use a few constant variables to store the minimum and maximum scores and their counts. The size of these variables does not depend on the size of the input array.