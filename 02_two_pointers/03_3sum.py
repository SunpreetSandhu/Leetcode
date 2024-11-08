'''

Intuition:
The problem requires finding all unique triplets in an array that sums to 0. To solve this efficiently we can leverage sorting and 2 pointer technique. We need to fix one element at a time then find the other 2 using a 2 pointer approach, which will avoid 3 nested loops in brute force. The sorted array allows us to use pointers and skip duplicates easily. 

Approach:
1)Sort the input array nums
2) Define ret as empty array
3) Loop through from i=0 to len(nums)
    a) If current element is same as prev element (and i>0), skip this iteration to avoid duplicates
    b) Define left as one element infront of the current num, and right as the last element in the array
        i)Calculate the 3sum of num+num[l]+num[r]
        ii)if this 3sum<0 increment l, if 3sum<0 decrement r
        iii)If the sum equals zero, record the triplet and increment the l pointer, skipping over duplicate values to ensure uniqueness.
4) return ret

Time Complexity: O(n^2) -> Looping through the list recording num, then looping again to find 2sum values that added to the first would = 0. 
Space Complexity: O(n) -> Due to the sort

'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()

        ret = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums)-1
            while l<r:
                threeSome = nums[i] + nums[l] + nums[r]
                if threeSome < 0:
                    l +=1
                elif threeSome > 0:
                    r -=1
                else:
                    ret.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return ret


        