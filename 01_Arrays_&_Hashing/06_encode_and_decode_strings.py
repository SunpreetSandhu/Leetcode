'''
Intuition:
This problem requires designing encoding/decoding mechanism for 
a list of strings. The encoded format needs to be a single string
in such a way that we can decode it back to its original form. We
can accomplish this by encoding it with the strings length and a 
delimeter '#', so when we decode, when we reach the #, we will know
that is one string in the list.

Approach:
1)We will define our encode method by initially setting encoded to an empty string 
then we will loop through the list of words
    i)Save the length of the word and concatenate encoded with length+'#'+word and return encoded string after looping
2)In decode, we will define an empty array and pointer i to be 0
    i) We will loop as long as i<len(encoded)
    ii)Set a second pointer j = i and loop/increment j until encoded[j] == '#'
    iii)Calculate the length as encoded[i:j], and update i to j+1 so i is at the first letter of the string
    iv)append the decoded string as encoded[i:i+length], where i is the start of word, and i+length is right after the last letter, this will append UPTO but not inclu i+length
    v)update i to be i+length, so it starts where the next string's length starts
    vi)after i has exceeded len(encoded), return the encoded list of strings


Time Complexity:
encoding:O(n) - we are looping through word in strs, jumping by word each time
decoding:O(n) - we are looping through encoded string but we jump the length of word each time so O(n) where n is length of original list of strings

Space Complexity: 
encoding:O(n) - encode strings length dependent upon length of all strings in strs
decoding:O(n) - we are creating decode array that is essentially gonna be same size as original

'''

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            length = str(len(word))
            encoded += length + '#' + word
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j]!='#':
                j +=1
            length = int(s[i:j])
            i = j+1
            decoded.append(s[i:i+length])
            i +=length
        return decoded





