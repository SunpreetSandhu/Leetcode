'''
intuition:
We will run a binary search algorithm. Divide the search into 2 every time. Declare a left and right pointer initially at start and end of array, and find middle of 2. Guess the middle value at the array and if guess is larger than intended value, update right pointer to mid-1 and if guess is smaller than target, update left pointer to mid+1, if both cases arent true, return the current index, mid. We will cut the loop off when the left crosses the right.

approach:
1) Declare left and right pointers, with left being 0 and right being last index of the array
2) loop through list as long as left less than or equal to right. 
    a)Calculate a mid point of left + right // 2.
    b) if the value of nums at midpoint is greater than the target, right is updated to mid-1, if the val of nums at midpoint is less than target, left is updated to mid+1. Return mid if none of those 2 conditions are true

time complexity:
O(logn) : we divide the search in half every time, 

Space complexity:
O(1): only 2 variables to keep track of mid with constant time operations
 
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left, right = 0, len(nums) -1

        while left<=right:
            mid = (left + right) // 2
            if (nums[mid]>target):
                right = mid - 1
            elif (nums[mid] < target):
                left = mid + 1
            else:
                return mid
        return -1