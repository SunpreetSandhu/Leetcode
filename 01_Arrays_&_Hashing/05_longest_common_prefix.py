'''
Intuition: Need to find the longest common prefix among an array of strings. A prefix is the longest common sequence of strings including the first letter. We can compare each character in each word at the same index until a mismatch occurst. If a character iny word at index i does not match the corresponding character in the first word we return the prefix found so far.

Approach:
1) Define an empty string ret, in the case where there will be no common prefix we will just return this
2) Iterate through the length of the first string and keep track of the index i
    a) Iterate through each word in the input strs
        i)If the length of the word is the same length as our index i, we know we have reached the end of the common prefix and will just return ret so far
        ii)If the character in the word at index i is not equal to the character at index i in the first word, we can return ret so far since the longest common prefix has been reached
    b) Add the character to ret as the characters are still common among the words
3) Return ret (this is the case where the first word is empty)

Time Complexity: O(m*n) -> m is the length of the first word and n is the number of words in strs. We iterate through the first word and for each character we iterate through the entire words in strs to check if that character matches in everything at the index i

Space Complexity: O(m) -> m is the length of the longest common prefix. In the worst case m is the length of the shortest word s, m<=s, the upperbound of the longest common prefix is the length of the shortest word in strs, s.
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ret = ""
        for i in range(len(strs[0])):
            for word in strs:
                if len(word) == i or strs[0][i] != word[i]:
                    return ret
            ret += strs[0][i]
        return ret


        
        