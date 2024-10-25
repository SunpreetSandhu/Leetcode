'''
Intuition: 
We need to find k most frequent elements given an array nums and we need an efficient way to get the k elements with highest frequency. We can use a BUCKET SORT inspired approach where we group the elements based on their frequency, for example index 6 in the bucket will correspond to the element that appears 6 times.After we have this bucket, we can loop backwards and extract the k elements

Approach:
1)Count the occurance of each element using hashmap with key = num, val = freq
2)Initialize buckets array to be initially empty array for each index, and we will initialize len(nums)+1 indexes, since we want the index of the bucket to correspond to the freq. Loop through the hashmap.
    a) Store the hashmap's freq at that particular key, and append the key to index in buckets corresponding to freq
3)Initialize result array initally empty, and loop backwards from len(buckets)-1, (since if buckets is length 7, buckets[7] would be out of bounds so we need to do -1).
    i)If there is a value at buckets[i], we will EXTEND the reusult array to add all the values that are in that frequency. We will then check if k elements have been reached, if so we return result up to k elements.
4) Return resu

Time complexity: O(n) - O(n) to iterate through nums, O(m) to iterate through hm where m is unique elements, O(n) to iterate through buckets in the worst case, overall O(n+1)

Space Complexity: O(n) - O(m) for hm in worst case, O(n+1) for buckets, O(k) for resu. Overall O(m+n+1+k), ie O(n)
'''

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hm = {}
        for num in nums:
            if num not in hm:
                hm[num] = 1
            else:
                hm[num] +=1
        buckets = [[] for i in range(len(nums)+1)]
        for key in hm:
            freq = hm[key]
            buckets[freq].append(key)
        resu = []
        for i in range(len(buckets)-1, 0, -1):
            if buckets[i]:
                resu.extend(buckets[i])
            if len(resu)>=k:
                return resu[:k]
        return resu

        