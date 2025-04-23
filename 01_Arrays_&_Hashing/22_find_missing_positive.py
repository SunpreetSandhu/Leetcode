'''
Intuition:
The problem asks us to find the smallest positive integer in the unsorted array. Since we only care about positive integers from 1 to len(nums), we can use the array itself to store state and mark presence of those values without the need for extra space. 

Approach:
1)Ignore irrelevant values:
    a)Replace all negative numbers with 0s since they’re not useful
2)Mark presence:
    a)For every valid number val in range [1,n], where n is len(nums), we mark the index val val-1 to a negative value to indicate val exists
    b)If the target index has a positive number we just switch it to negative to indicate the presence of that index-1 in the array
    c)If it’s a 0 it can’t be flipped so we set it to a negative high number (so we don’t come back to this fake value as it’s not in range[1,n], but we will still see the presence of that index-1 since it’s negative) (-(n+1)).
3)Find missing positive:
    a)After marking step, we scan through the array. The first index i that contains a non negative value means the number i+1 is missing
4)If all positions are marked, return n+1 as the smallest positive 

Time Complexity: O(n) -> One pass to sanitize negatives, one pass to mark values, one pass to find result
Space Complexity: O(1) -> Modified the array in place
'''
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i]<0:
                nums[i] = 0
        
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1<=val<=len(nums):
                if nums[val-1]>0:
                    nums[val-1] *= -1
                if nums[val-1]==0:
                    nums[val-1] = -1*(len(nums)+1)
                    
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i+1
        return len(nums)+1

                
            


        