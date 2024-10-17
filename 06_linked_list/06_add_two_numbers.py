# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        
Intuition:
We are tasked with adding 2 nums represended by 2 LL, each node contains a digit fo the number in reverse order. Goal is to return the sum as a new LL, also in reverse. To solve this we can simulate a manual addition process digit by digit and handling the carry over when the sum exceeds 9. Edge cases are when one of the lists are smaller or when both LL are only of length 1 and it has a carry. 

Approach:
1) Create a dummy node to serve as the starting point of the new LL.
2) Set carry variable initially to 0
3) Loop through the LL, so long as both l1 and l2 arent null or if theres a carry (to handle the case where l1 and l2 are null but theres a carry)
    a)initialize variables v1 and v2 to 0 and only if l1 exists, set v1 to l1.val and vice versa
    b)set variable val to v1+v2+carry
    c)Update carry to floor division of val // 10 as the value to carry
    d)Update val to the remainder of val%10, as next node value
    e)Add a new node with value val as the next node
    f) Update curr, and update l1/l2 if they are not null
4) Return dummy.next

Time Complexity: O(n): We loop through the longest of the 2 lists, once

Space complexity: O(n): We create a new list that is as long as the longest input list l1 or l2




        """
        dummy = ListNode()
        curr = dummy

        carry = 0
        while l1 or l2 or carry:
            v1,v2 = 0,0
            if l1:
                v1 = l1.val
            if l2:
                v2 = l2.val
            val = v1+v2+carry #ex: 4+6+0 = 10
            carry = val // 10 #floor division to find carry
            val = val % 10 #find remainder for the actual value written
            curr.next = ListNode(val)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next


        