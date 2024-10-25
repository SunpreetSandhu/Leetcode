'''

Intution:
We need to group a list of strings where each group consists of anagrams. Two words are anagrams if they have the same character frequencies. By representing each word with its character frequency, we can use that frequency as a key in a hashmap. The value in the hashmap will be a list of words (anagrams) that share the same key. For each word, we count the frequency of its letters, use this frequency count as the key, and add the word to the corresponding group in the hashmap. The frequency will initally be stored as an array, later converted to tuple to put in hashmap.

Approach:
1)Create an empty hashmap
2)Loop through the words array
    a)Create an array of 0s of size 26 to reflect the alphabet
    b)Loop through each char in the word
        i)Increment the index of the array that corresponds to the ascii value (ord(char) - ord(a)), to update the freq. For ex index 1 corresponds to letter b. 
    c)Convert the array to a tuple (since hashmap keys cant be arrays)
    d)Check if the key has not been created yet in the hashmap, if so, initialize the value at that key to an empty array (to avoid a key error since we are appending)
    e)Append the hashmap at the key corresponding to the tuple, and value being the word itself
3)Return all the values in the hashmap ie hashmap.values()

Time Complexity: O(n*k): n is the words in the array and k is the avg chars in each word

Space Complexity: O(n): since worst case our hm keys map to each word. Here, keys take constant space of tuple size 26 so more specifically it is O(26*n), so overall O(n)

'''

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hm = {}
        for word in strs:
            count = [0]*26
            for char in word:
                count[ord(char) - ord('a')] +=1
            key = tuple(count)
            if key not in hm:
                hm[key] = []
            hm[key].append(word)
        return hm.values()
        


        