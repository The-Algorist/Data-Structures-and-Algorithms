## Python Code for Checking Nearby Duplicates

This file provides the Python code for checking if there are any duplicate numbers within a specified distance in an array. The code adheres to best practices for algorithm explanation and Markdown formatting suitable for GitHub.

**Problem:**

Given an integer array `nums` and an integer `k`, determine if there are two distinct indices `i` and `j` in the array such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

**Solution:**

This solution utilizes a dictionary and iterates through the array to find duplicate numbers within the specified distance `k`:

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i
        return False
```

**Explanation:**

1. **Dictionary:** An empty dictionary `seen` is created to store the latest index of each encountered number.
2. **Iteration:** The code iterates through the `nums` array using `enumerate` to access both elements and their indices.
3. **Duplicate Check:** For each number, we check if it exists in the `seen` dictionary:
    - If present, and the difference between the current and previous indices (`i - seen[num]`) is less than or equal to `k`, it indicates a duplicate within the allowed distance, and `True` is returned.
4. **Index Storage:** If the number is not yet seen, its current index is stored in `seen` for future reference.
5. **No Duplicates:** If the loop finishes without finding duplicates within `k` distance, `False` is returned.

**Time and Space Complexity:**

- Time: O(n):
   The main loop iterates through each element of the array once, contributing O(n) time complexity.
   Checking for the existence of a number in the dictionary using "in" is considered constant time, O(1) on average.
   Even though there could be multiple lookups for the same number in the worst case, the total number of lookups still scales linearly with the array size, hence O(n).

- Space: O(n):
   The dictionary stores the most recent index for each number encountered. In the worst case, every element in the array could have a different index stored, leading to a space complexity of O(n).

This solution offers efficient duplicate detection with linear time and space complexity.

**Additional Notes:**

- The `enumerate` function allows simultaneous iteration over elements and their indices.
- The code uses `abs(i - seen[num]) <= k` to ensure duplicates are within the specified distance.



