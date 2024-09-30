# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
Intuition: 
We need to reverse a linked list. We will use a two pointer algorithm, with the a curr and prev pointer.
Initially, prev will point to None, and curr will point to head. We want our curr.next to point to prev. prev will update to our curr value. 
our original curr.next to be the new curr value.

Approach:
1) Initialize prev and curr to be None and head respectively
2) Loop through the linked list until curr isnt None
    a)Keep reference of the curr.next variable and store it in a var nxt
    b)Change curr.next to be pointing to prev
    c)update prev to curr and update curr to our nxt value
3) Return prev as the new head of the list, as it will point to the last val of the original linked list

Time Complexity:
O(n) where n is the num of nodes of the linked list

Space Complexity:
O(1) 

'''
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

   
        prev = None
        curr = head

        while curr:
            nxtNode = curr.next
            curr.next = prev
            prev = curr
            curr = nxtNode
        return prev
