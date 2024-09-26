'''
Intuition: To determine if a string is a palindrome, it has to read the same from forward and backward, ignoring non-alphanumeric chars and case. We will first cleanse the string to only inclu alphanum chars and convert all chars to same case then use 2 pointers to compare chars from begenning to end moving towards center, and exit loop when a cross occurs

Approach:
1) Filter out all non -alphanumeric chars from string and convert the remaining chars to uppercase forming a new string
2) initialize 2 pointers, left and right
3) Use while loop with exit condition when left crosses right.
    a)If theyre equal, we increment left and decrement right
    b)If theyre not equal we return false
    c) once left crosses right, we return true since we checked all chars

Time complexity:
O(n): more specifically n (conversion) + n/2 (looping over string)

Space complexity:
O(n): in worst case storing the cleaned version of string is exactly the size of n
'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alnum_string = ''.join(char for char in s if char.isalnum())
        newstring = alnum_string.upper()
        lp = 0
        rp = len(newstring) - 1
        

        while lp<rp:
            if(newstring[lp] != newstring[rp]):
                return False
            lp +=1
            rp -=1
        return True
