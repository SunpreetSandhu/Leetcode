'''
Intuition: This problem involves us creating a stack that in addition to standard stack operations, can retrieve the minimum element in constant time. This is achieved by maintaining a second stack that tracks the min value at each level of the stack. The minStack will also push/pop every time the main stack does to maintain it at each level

Approach:
1. Use 2 stacks, one for standard operations (push,pop,top), and the minStack for keeping tack of minimum element at each point
2. Push: 
    a)We first push onto the main stack
    b)Before pushing onto the minStack, we see if the new val is less than the top of the stack, if it is we push that, if the minStack is empty, we just push the val
3. Pop: We pop from both the main and minStack
4. Top: We return the main stack's top element 
5. getMin: We use the minStack's top element as that is the current minimum

Time Complexity:
O(1) - all operations are done in constant time, the getMin is constant due to the use of the extra stack

Space Complexity:
O(n) - we have stack and minStack which grow proportionally as we push
'''

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if self.minStack:
            val = min(val, self.minStack[-1])
        self.minStack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minStack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()