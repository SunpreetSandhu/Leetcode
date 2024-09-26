'''
intuition: We will store all opening parantheis in a stack, and pop off the stack if the closing parenthesis matches the latest added opening parenthesis in the stack. We will maintain this mapping of closing and opening parenthises through a hashmap. We will reject if a closing parenthesis has been added on an empty stack or if the final stack is not empty.

Approach:
1) Define an empty stack, and a hashmap with keys being closing bracket and values of opening bracket. 
2) Loop through the input string. If the value is a key in the hasmap, ie is a closing bracket we will:
    a) if stack is empty return false as closing bracket on empty string is invalid
    b) if not empty, we will check if the top of the stack is equal to the value of the hashmap at the key ie the associated opening bracket. If yes, we will pop from the stack
3) In the end check if stack is empty, if yes return true otherwise false

Time complexity:
O(n) as we are looping through the input string

Space complexity:
O(n) as in the worst case input string contains only opening brackets and stack is O(n)

'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        hm = {')' : '(', ']':'[', '}':'{'}

        for bracket in s:
            if bracket in hm: #if its a key ie closing bracket
                if not stack: #stack empty + closing bracket = false
                    return False
                else: #check top of stack vs opening bracket assoc to closing
                    if stack[-1] == hm[bracket]: 
                        stack.pop()
                    else:
                        return False
            else:
                stack.append(bracket) #bracket value is an opening bracket
        if len(stack) == 0:
            return True
        return False
