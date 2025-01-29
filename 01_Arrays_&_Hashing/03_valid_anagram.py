class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        Intuition: To determine if 2 strings s and t are valid anagrams, we     need to ensure the frequency of each letter in both strings are equal. We can do this by using 2 hashmaps with the frequency of letters for each string. If the 2 hashmaps are equal the strings are valid anagrams

        Approach:
        1) Immediately return false if the length of the 2 strings are different
        2) Get the frequencies of both s and t in 2 hashmaps
        3) Check if the 2 hashmaps are equal, if yes return true, otherwise return false

        Time complexity: 
        O(n) or more specificly O(s+t). 

        Space complexity:
        O(n) as size of both hashmaps are porportional to s and t
        """
        if len(s) != len(t):
            return False
        countLetters1 = {}
        countLetters2 = {}

        for letter in s:
            if letter not in countLetters1:
                countLetters1[letter] = 1
            else:
                countLetters1[letter] += 1
        for letter in t:
            if letter not in countLetters2:
                countLetters2[letter] = 1
            else:
                countLetters2[letter] += 1
        return countLetters1 == countLetters2