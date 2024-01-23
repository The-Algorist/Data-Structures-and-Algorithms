class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merges two sorted arrays nums1 and nums2 into nums1 in-place, preserving the sorted order.

        Args:
            nums1: The first sorted array, with m elements.
            m: The number of elements in nums1 to consider (its valid size).
            nums2: The second sorted array, with n elements.
            n: The number of elements in nums2.

        Returns:
            None. Modifies nums1 in-place to contain the merged result.
        """

        # Initialize pointers for tracking positions in the arrays:
        k = m + n - 1  # Pointer for placing merged elements in nums1 (starts at the end)
        i, j = m - 1, n - 1  # Pointers for traversing nums1 and nums2 (start at their ends)

        # Iterate while there are still elements in nums2:
        while j >= 0:
            # Compare elements from nums1 and nums2, starting from their ends:
            if i >= 0 and nums1[i] > nums2[j]:
                # If the element in nums1 is greater, place it at the current position in nums1:
                nums1[k] = nums1[i]
                i -= 1  # Move the nums1 pointer backward
            else:
                # Otherwise, place the element from nums2 at the current position in nums1:
                nums1[k] = nums2[j]
                j -= 1  # Move the nums2 pointer backward
            k -= 1  # Move the merged elements pointer backward
