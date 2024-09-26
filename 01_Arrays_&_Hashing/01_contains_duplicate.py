class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        intuition: use hashset since it has add  function.
        
        We will check if a num from the nums is already in hs, if not add it in
        If its already in, we return true and exit if not then we return false after going through all numbers in nums

        approach:
        1. initialize empty hashset
        2. iterate through all the nums in nums
            -if the number already exists in hs then return true and exit
            -if not, add it to the hs
        3. after iterating through everything, and code hasnt exited on true, return false

        time complexity:
        O(n) to iterate through all num in nums

        space complexity:
        O(n) - hash set can potentially have ALL the elmeents from nums
        """

        hs = set()

        for num in nums:
            if num in hs:
                return True
            hs.add(num)
        return False
