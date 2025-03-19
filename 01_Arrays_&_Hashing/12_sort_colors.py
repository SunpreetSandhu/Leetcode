'''
Intuition:
The problem requires sorting an array of 3 distinct elements (0,1,2) in place. We can use bucket sort but that would require more than 1 pass through the array. Instead we can partition the array into 3 sections for 0s, 1s, and 2s using 3 pointers. We can move all the 0s on the LHS, and all the 2s on the RHS. 

Approach:
1) Our 3 pointers are l, r, and i. The first, l, will track the next position to place a 0, whereas r will track the next position to place a 2 and i iterates through the list to check elements.
2) If nums[i] is 0, we swap it with the element that l points to. After doing so we increment l and i
3)If nums[i] is 1, we simply increment i
4) If nums[i] is 2, we swap it with the element that r points to. After doing so we decrement r. We do NOT increment i here as we need to reevaluate the element coming from r since it has not been checked before.

Time Complexity: O(n) -> We are doing a single pass through the array, performing constant time operations
Space Complexity: O(1) -> We are using constant space (3 pointers), and all operations performed in place, no extra memory used
'''

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        
        l = 0
        r = len(nums)-1
        i = 0
        while i<=r:
            if nums[i] == 0:
                swap(i,l)
                l+=1
                i+=1
            elif nums[i] == 1:
                i+=1
            elif nums[i] == 2:
                swap(i,r)
                r-=1
        


        