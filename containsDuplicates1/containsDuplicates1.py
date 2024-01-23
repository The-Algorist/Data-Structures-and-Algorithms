class Solution:
   """
   Class containing a method to check for duplicates in a list of integers.
   """

   def containsDuplicate(self, nums: List[int]) -> bool:
       """
       Checks if a given list of integers contains any duplicates.

       Args:
           nums: The list of integers to check for duplicates.

       Returns:
           True if the list contains duplicates, False otherwise.
       """

       # Create a set to efficiently track unique elements:
       seen = set()  # Sets provide fast membership checks

       # Iterate through each number in the list:
       for num in nums:
           # Check if the current number has already been seen:
           if num in seen:
               return True  # Duplicate found, return True immediately

           # If not seen before, add it to the set of seen numbers:
           seen.add(num)

       # If the loop completes without finding duplicates, return False:
       return False  # No duplicates found
