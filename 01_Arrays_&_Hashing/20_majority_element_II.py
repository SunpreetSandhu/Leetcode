'''
Intuition:
The task is to find all elements in the array that appear more than ⌊n/3⌋times. An important insight is that thre will be at most 2 such elements in an array. This solution uses an elimination strategy (similar to Boyer-Moore voting algorithm), where we wil maintain candidate frequencies in a hashmap. As we iterate through the array, we’ll update the counts and ‘eliminate’ candidates when the hashmap has more than 2 elements being tracked. After the elimination phase, we’ll perform a final pass to check which candidates truly appear more than ⌊n/3⌋ times, as even if the final hashmap has 2 elements, they may not appear more than ⌊n/3⌋ times leaving us with no solution.

Approach:
1)Candidate Elimination
    a)Initialize hashmap hm that maps numbers to their respective frequency counts (not real frequencies but rather a temporary count used for candidate elimination during the traversal)
    b)Iterate through each number in nums, and for each number increment the count in hashmap. 
    i)If the hashmap contains more than 2 keys, we create a new hashmap hm2 by iterating over the entries in hm and adding each key with its frequency reduced by 1. Any key whose updated frequency becomes 0 is not added to hm2 simulating a removal. We will then replace the original hashmap hm with hm2
2)Verification
    a)Once the elimination phase is complete we will compute the threshold value of ⌊n/3⌋ (val)
    b)For each candidate in hm we will get its frequency from nums using nums.count(candidate). If this value is greater than val, we will append it to the result array
3)Return
    a)Return result array 

Time Complexity: O(n) -> We are iterating through the array in the candidate elimination phase and during the verification phase, nums.count(candidate) is a O(n) operation, and we are doing it at most twice.

Space Complexity: O(1) -> No extra memory used apart from hashmap which is at most of size 2
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hm = defaultdict(int)
        for num in nums:
            hm[num] +=1
            if len(hm) <=2:
                continue
            hm2 = defaultdict(int)
            for n,c in hm.items():
                if c>1:
                    hm2[n] = c-1
            hm = hm2
        res = []
        val = len(nums)//3
        for num in hm:
            if nums.count(num) > val:
                res.append(num)
        return res


        
        


        