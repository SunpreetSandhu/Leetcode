'''
Intuition:
This problem requires us to find the length of the longest sequence of consecutive int in an unsorted array. We can find the longest sequence by finding the start of the array. A number is the start of the array if there is no number n-1 in the array. If this is true, we will count how manu consecutive numbers follow this start and update the longest sequence value. We can first store all numbers in a hashset, then we will loop through the array, see if the number-1 is in the hashet, if it is not then we will iterate until the sequnce is done and update longest length.

Approach:
1) Initialize a hashset of nums, and variable longest to 0
2) Loop through all nums in array
    a)If num-1 is not in the hashset we are at the start of the sequence
        i)Define internal variable length to calculate the length of that sequence initally set to 0
        ii)Loop until num+length is in the hashset, if it is increment length by 1
        iii)Update longest if length is greater than longest
3)Return longest

Time Complexity: O(n) - we loop through nums in the outer loop, and the inner loop is actually only executed when we are at the START of a subsequence and not for every number, so we visit each number in the array at most twice, so overall O(n)

Space Complexity: O(n) - we define hashset with nums
'''

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        hs = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in hs:
                length = 0
                while num+length in hs:
                    length +=1
                longest = max(longest,length)
        return longest

        