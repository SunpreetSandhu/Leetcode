# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Intuition: We need to reorder a SLL so that the nodes alternate between the first and last nodes. This can be broken down into 3 parts. 
1) Find the middle of the list using slow/fast pointer algorithm
2)reversing the second half to prepare it for merging
3) merge the two halves alternating between the nodes from first and reversed second half to reorder the list

Approach:
1) Find the middle of the list:
    a) Declare slow and fast pointers pointing to the head and head.next of the list
    b) Perform the slow/fast pointer algorithm looping through the SLL, and stopping when fast either reaches the last node or null. Increment slow by one node and fast by 2. 
    c)Assign variable second which is the head of the second linked list to slow.next as slow ends at the node before the second half, and assign slow.next to None, as slow is the last node in the first half this will cut off ties to the second half

2) Reverse the SLL:
    a)Perform the reverse algorithm, set prev to none, loop through till second is None, hold nxtVal temporary variable for second.next, set second.next to prev, update prev to second, update second to the temporary nxtval.
    b) Declare variable first to head as it is the head of the first half and second to prev as prev is currently poinitng to the head of the reversed second half

3)Merge the two SLL one by one:
    a) Loop through until second is Null, as second is always smaller than or equal to first half
        i)declare two temporary values to store the first.next and second.next nodes
        ii)set first.next to second
        iii)set second.next to the first temporary variable
        iv) update first to the first temp variable and second to the second temp variable

Time complexity: O(n) -> more specifically O(n/2), as we only go through half the input but simplifies to O(n)

Space complexity: O(1) -> in place reordering of nodes no extra memory
'''
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.

        1->2->3->4
        s  f 

        
        1->2->None  3<-4
           s     f 

        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next #new head for the second list
        slow.next = None
          
        #reverse second half
        prev = None
        while second:
            nxtVal = second.next
            second.next = prev
            prev = second
            second = nxtVal
        second = prev
        first = head

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2





        