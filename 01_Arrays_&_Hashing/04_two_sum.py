'''
Intuition: We need to find 2 indices in an array where the 2 values sum to the given target. A brute force way would be to iterate over all pairs being O(n^2). Instead we can use a hashmap, where the key will be the number itself and the value of the index, since hashmap lookups are O(1).

Approach:
1) Define an empty hashmap
2) Iterate through the array
    a)The number num2 is target - nums[i]
    b)If num2 is in our hashmap, return that index and the current nums index
    c)If num2 is not in the hashmap, we will store nums[i] in our hashmap with the index

Time Complexity: O(n) -> Iterating through nums, and performing hashmap lookup which is O(1)

Space Complexity: O(n) -> Hashmap proportionally increases with nums
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hm = {}
        for i in range(len(nums)):
            num2 = target - nums[i]
            if num2 in hm:
                return [hm[num2], i]
            hm[nums[i]] = i
            


        