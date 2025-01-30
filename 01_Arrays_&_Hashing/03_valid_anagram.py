'''
Intuition:
An anagram is a word that is formed by rearanging the letters of the original word. So both words have the same character frequency. Instead of sorting (O(nlogn)), we can use a fixed-size frequency array to track character occurences in O(n) time

Approach:
1) Check if both words have the same length, if not return False
2) Initialize an empty array of size 26 for frequencies of letters
3) Iterate through the length of the word, and increment the frequency array for letters in s and decrement for letters in t 
4) Iterate through the frequency array to ensure it's empty, if not return False

Time Complexity: O(n) -> Iterating through the length of input word

Space Complexity: O(1) -> No extra space used just a fixed size frequency array
'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -=1
        
        for num in count:
            if num != 0:
                return False
        return True



        