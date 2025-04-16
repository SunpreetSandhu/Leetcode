'''
Intuition:
We want to count the number of contiguous subarrays whose sum equals the target value k. The key insight is to use the prefix sum technique, as we traverse the array we’ll maintain a cumulative sum upto that point. At each step we’ll check if there exists a previous prefix sum such that curSum - k exists in a hashmap. If it does it means there’s a subarray ending at the current index whose sum is k and we add the frequency of that prefix sum to the result. This works because cutting the earlier prefix sum from the current sum isolates a subarray that sums to k. To efficiently track these sums we’ll store prefix sums and their frequencies in a hashmap.

Approach:
1)Initialize a hashmap and set the 0 value frequency to 1 since a prefix of sum 0 occurs before any processing. We will also define variables res and curSum
2)Iterate through the nums array
    a)Increment the curSum with the current num in nums
    b)If the curSum - k value exists in the hashmap, we will increment res with the frequency of curSum -k (this essentially means that we can reach the value k by cutting off a value from our subarray, the amount of times this value appears upto our current point  is stored in the hashmap).
    c)Increment the hashmap frequency of the curSum value
3)Return res

Time Complexity: O(n) -> We traverse the array once, with constant time operations
Space Complexity: O(n) -> Due to the hashmap growing linearly with input array
'''

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hm = defaultdict(int)
        hm[0] = 1
        res = 0
        curSum = 0
        for num in nums:
            curSum += num
            val = curSum - k
            if hm[val] > 0:
                res += hm[val]
            hm[curSum] +=1
        return res
            

        