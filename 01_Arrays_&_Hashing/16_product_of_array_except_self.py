'''
Intuition
We need to compute an array where each element at index i is the product of all the elements in the array except for nums[i]. Essentially prefix*postfix(all nums before, and after), is the desired value. A direct approach where we compute all elements except nums[i] and calculate their products would be O(n^2). We can also have a prefix and postfix array, and multiply the 2 and store value in output, but this would be O(n) space comp. In order to achieve O(n) time comp and O(1) space, we can initially store prefixes in output, then compute postfixes*prefix on output itself. 

Approach:
1)Initally set output array to all 0s
2)Set prefix var to 1 (since first val has no prefix) and loop from 0 to len(nums)
    a)set output[i] to prefix
    b)update prefix by multiplying it by nums[i]
3)Set postfix var to 1 (since last val has no postfix) and loop from the end of list to start:
    a)set output[i] to postfix * output[i]
    b) update postfix by multiplying it by nums[i]

Time Complexity:
O(n) - looping over nums twice

Space complexity:
O(1) - since output array doesn't count, we aren't using any other extra non constant space
'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [0 for i in range(len(nums))] 
        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix = prefix * nums[i]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] = output[i] * postfix
            postfix = postfix *nums[i]
        return output
   
        

