'''
Intuition: The goal is to remove all occurences of a number (val) from the array in place and return the new length of the array. We don't actually need to 'remove' the numbers, we can just overwrite them using 2 pointers:
    A left pointer (l) that tracks the position where the next non-val element should be placed
    A right pointer (r) that iterates over the array and checks for values not equal to val

Approach:
1) Initialize left pointer (l) which tracks where to place the next non-val number
2) Iterate through the array, and for any non-val value place it at the left pointer index, and increment the left pointer
3) Return the left pointer which represents the number of non-val numbers

Time Complexity: O(n) -> Just iterating through nums once

Space Complexity: O(1) -> All done in place, no extra memory
'''

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l+=1
        return l
        