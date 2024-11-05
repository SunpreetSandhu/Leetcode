'''
Intuition: The goal is to find two numbers in the array such that their sum adds to the target. The soln must return 1-based indexes of the 2 numbers and use O(1) space complexity. The sorted nature of the array suggests that we can use a 2 pointer soln. Pointer 1 starts at beginning of array and pointer 2 starts at the end of the array. If the sum of the 2 pointers is equal to the target, we return the indexes, if the sum is less than the target, we move the left pointer by 1 (since we need to INCREASE the sum), if the sum is greater than the target we move the right left by 1 (since we need to DECREASE the sum)


Approach:
1)Initialize left pointer to 0 and right to the last index in input
2)Loop until left is behind right:
    a)If the sum of the array at the indexes of l and r is equal to the target, return the 1 based indexes
    b)If the sum is less than target, we increment l by 1
    c)If the sum is greater than target, we decrement r by 1

Time Complexity:
O(n) -> The loop runs while l < r, meaning in the worst case, we move each pointer across the array exactly once. Thus, each element is processed at most once, and the total time complexity is linear, O(n).

Space Complexity:
O(1) -> No extra space is used as we just have pointers
'''

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(numbers)-1

        while l<r:
            curr = numbers[l]+numbers[r]
            if curr == target:
                return [l+1, r+1]
            elif curr < target:
                l+=1
            elif curr > target:
                r-=1
        

        