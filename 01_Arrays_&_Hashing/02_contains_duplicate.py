'''
Intuition: We need to find if the given array contains a duplicate. The straightforward way would be to check each individual element, but this would be O(n^2). Instead we can use a hashset and if the new elmeent is already in the hashset we will know there's duplicates

Approach:
1. Initialize hashset: initialize an initially empty hashset
2. Iterate through the array: For each element in the array;
    a)If it is not in the hashset add it 
    b)If it is already in the hashset, return True indicating a duplicate value
3. After all iterations, we can now return False

Time Complexity: O(n) -> Iterating through the array at most once and just performing constant time operations like adding to the hashset
Space Complexity: O(n) -> The hashset grows proportionally to the input array

'''

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        hs = set()
        for num in nums:
            if num not in hs:
                hs.add(num)
            else:
                return True
        return False
        