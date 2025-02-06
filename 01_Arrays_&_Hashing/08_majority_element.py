'''
Intuition:
The goal is to find the majority element in a list, which appears more than n/2 times (n is length of list). We can simply caluclate the number that appears the most with a hashmap but this would require O(n) space. To do it in O(1) space we can use the Boyer-Moore voting algorithm since we know there will always be an element that appears more than half the list and will OUTNUMBER all other elements. This algorithm works by maintaining a "candidate" element and a counter. The majority element will outnumber all other elements, so the counter will reflect it.

Approach:
1) Initialize count = 0 and candidate = None
2)Iterate through nums
    a)if count is 0, the current element will become our new candidate
    b)If the current element is our candidate increment count
    c)If the current element is NOT our candidate decrement count
3) Return the final candidate after the loop

Time Complexity: O(n) -> Iterating through nums
Space Complexity: O(1) -> No extra space used
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = 0
        candidate = None

        for i in range(len(nums)):
            if count == 0:
                candidate = nums[i]            
            if nums[i] == candidate:
                count +=1
            else:
                count -=1
        return candidate

        