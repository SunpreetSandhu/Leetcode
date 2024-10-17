'''
Intuition: We are given two sorted linked lists and we need to return the head of the sorted merged linked list. We will compare the heads of each linked list and add the node if it is smaller and go to the next node as the lists are already sorted

Approach:
1) Create a dummy node to avoid edge cases such as an empty linked list. We will also define a tail variable to initially point to dummy, but will eventually point to the newest added node as we build the merged linked list
2) We will loop while both list1 and list2 are not empty. 
    a) If list1 has value less than list2, we will add that node into the merged list (tail.next, continuing from the dummy). We will update list1 to list1.next to point to the next node
    b) If list2 has value less than list1 we will add that node into the merged list. We will update list2 to list2.next to point to the next node
    c) finally, we will update tail to tail.next and continue the next iteration
3) If after the loop, list1 or list2 still have nodes, add them all to the merged list (tail.next)
4) Return dummy.next, as this was the first added node and the head of the merged list (in empty edge cases it will be null)



Time Complexity: O(n), more precicely O(n+m) where n and m is the amount of nodes in list 1 and list2, as we may have to traverse both in the worst case.

Space Complexity: O(1): The returned merged list is not creating a new linked list rather it rearanes list1 and list2 in place without assigning a new linked list

'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next 
        