'''
intuition: To find the 2 numbers that sum to the target, we can essentially look backwards using a hashmap. We can do target - current number to find what that 2nd number will be, then if its in the hashmap as a key we can return the 2 indexes otherwise we will continue adding the current number and index as key value pairs in the hashmap. The lookup will be O(1) as we just find the key. 

approach:
1) Initialize an empty hashmap to store the numbers and their corresponding indecies as key value pairs
2) Iterate through the list (dynamic array) nums.
    a)For each number nums[i] we will calculate its complement target - nums[i] and if the complement is already in the hashmap as a key, we found the 2 numbers and return their indeces [hm[target-nums[i]], i].
    b)If the complement isnt in the hashmap the curr number nums[i] and its index i is added to the hashmap, and we continue itterating

Time complexity:
O(n) as we will have to iterate through the entire list in the worst case

Space complexity:
O(n) as if we iterate through the whole list, well have to store it in the hm as we go along
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hm = {}

        for i in range(len(nums)):
            if target - nums[i] not in hm:
                hm[nums[i]] = i 
            else:
                return [hm[target-nums[i]], i]
            

        