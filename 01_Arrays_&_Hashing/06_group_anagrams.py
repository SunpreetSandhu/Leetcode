'''
Intuition: 
Need to group anagrams, can leverage the fact that 2 anagrams have identical character counts. Instead of sorting each word then comparing which will be O(n * klogk), we can represent each word as the character count in an array of size 26. This will be a unique key.

Approach:
1) Initialize hashmap where key = character count tuples, val = words (anagrams)
2) Iterate through each word
    a) Create a count array of 26 0s (for each letter)
    b) Iterate through each letter in the word, and populate it by getting the index of the letter using ord, and incrementing at that index
    c) Convert the count array to tuple (array is not hashable)
    d) If the key isn't in the hasmap, just set it to an empty array and append the word in (just append if key is in hashmap)
3) Return hashmap.values() (list of grouped anagrams)

Time Complexity: O(n * k) -> n: number of words, k:max length of word (letters)
Space Complexity O(n) -> hashmap can contain all words as keys

'''

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        hm = {}
        for word in strs:
            asci = [0 for i in range(26)]
            for letter in word:
                index = ord(letter) - ord('a')
                asci[index] +=1
            key = tuple(asci)
            if key not in hm:
                hm[key] = []
            hm[key].append(word)
        return hm.values()







        