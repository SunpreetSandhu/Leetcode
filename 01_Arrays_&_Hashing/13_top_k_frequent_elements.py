'''
Intuition:
The goal is to find the k most frequent elements in an array. The naive approach involves counting frequencies and then sorting the elements by frequency and selecting the top k. The sorting takes O(nlogn) time, and we can instead do a bucket sort approach in O(n) time by leveraging the frequency as an index, avoiding the sorting.

Approach:
1) Count Frequencies:
    a)Use a hashmap to count the frequency of each element in nums.
2) Bucket Sort by Frequency:
    a)Create a list of buckets where the index represents the exact frequency   (which is why we need len(nums) +1 buckets). Bucket i will store elements that appear i times, and elements will appear at most len(nums) times.

3) Extract top k elements:
    a)Iterate from the top of the buckets array down, and collect elements until the result contains k or more elements. When this happens we will print everything from the array not including the Kth element if its present

Time Complexity: O(n) -> Counting frequencies: O(n), Building buckets: O(n) (each unique element is processed once), Extracting top k: O(n) (worst case, all elements have unique frequencies)

Space Complexity: O(n) -> Worst case, all elements are unique and hash maps scales the input array, and also the bucket is O(n)
'''
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        hm ={}
        for num in nums:
            if num not in hm:
                hm[num] = 1
            else:
                hm[num] +=1
        
        bucket = [[] for i in range(len(nums) +1)]
        for key in hm:
            bucket[hm[key]].append(key)

        resu = []
        for i in range(len(bucket)-1, 0, -1):
            if bucket[i]:
                resu.extend(bucket[i])
            if len(resu)>=k:
                return resu[:k]
        return resu



        

        