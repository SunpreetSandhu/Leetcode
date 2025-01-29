'''
Intuition: We need to concatenate the array nums with itself, so the return array will be 2 * nums

Approach:
1) Define initially empty return value ans
2) Loop twice, and each iteration append every value of nums, so the resulting array will be 2*nums
3)Return the resulting ans array

Time Complexity: O(n) -> iterating through every value in nums 2 times, so specifically O(2n)
Space Complexity: O(n) -> resulting ans array is 2 * len(nums), so more specifically O(2n)
'''


class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans

        