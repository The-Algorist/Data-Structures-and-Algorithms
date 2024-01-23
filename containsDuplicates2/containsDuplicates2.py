class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # creating an empty dictionary
        dict = {} 

        # browsing through array
        for i, num in enumerate(nums):
            # If number is already present in the dictionary 
            # and the differeces of the indices is less than or equal to k
            # then return true value as that is the answer.
            if num in dict and i-dict[num] <= k:
                return True
            # store the current index of the number in the dictionary
            dict[num] = i
        # If no solution  exists while iterating, then return False
        return False