# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Intuition:
To remove the nth node from the end of a linked list a naive approach would be to find
the length of the list first, then calculate where that node lies and remove it, but this
would require 2 passses over the list. Instead we can opt for a 2 pointer, fast/slow method 
where the second pointer is n spaces apart from the first. Once the second pointer reaches 
null, we would have reached the node to remove. However, we need the node prior to the node to 
remove, so because of that and other edge case reasons, we will need a dummy node, and the left 
pointer will start from there.

Approach:
1) Initialize a dummy node right behind the head (set dummy.next to head)
2) Loop while decrementing n, and shifting right by one node until n is 0 or
   right has reached none
3)loop until right has reached none, and shift left and right by one each time
4)Since left is now at the node right before the node to remove, set the next val 
of it to the value that is next of the node to be removed, and set the remove nodes next
to null.
5) return dummy.next

Time complexity: O(n), we loop through the list once, until right reaches null

Space Complexity: O(1), as we did not assign a new variable that scales with the provided SLL, we did it in place
'''

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode()
        dummy.next = head

        left = dummy
        right = head

        while n>0 and right:
            right = right.next
            n -= 1
        while right:
            left = left.next
            right = right.next

        
        remove = left.next
        left.next = remove.next
        remove.next = None

        return dummy.next

