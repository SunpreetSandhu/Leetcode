'''
Intuition: We need to create a deep copy of each node in the linked list, where each node has a next and random pointer. The way we can approach this is creating a hash map where the original nodes will point to the new copied nodes. We will perform this with 2 passes, where the first pass will simply create the node copies and map them to the original nodes, and the second pass will create the next and random pointer for the copied nodes based on the the copied nodes that the original next and random map to

Approach:
1)We will create a hashmap with an initial mapping of none to none, to handle the cases where the next/random pointer will point to none  without getting a key error.
2)Loop through the linked list and map each old node to the new node copy
3)Loop through th elinked list and set the copied node's next value to the value of the copied node that the orignal node's next  maps to and vice versa for random
4) Return the head of the copied LL, ie the node that maps to the head of the orignal LL

Time Complexity: O(n), more specifically O(2n), due to 2 passes, but simplifies to O(n)

Space complexity: O(n), as we are mapping the LL values to a hashmap
'''


"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        oldToNew = {None: None}
        cur = head
        while cur:
            oldToNew[cur] = Node(cur.val) #mapping old to new
            cur = cur.next
        
        cur = head
        while cur:
            oldToNew[cur].next = oldToNew[cur.next]  #setting copied nodes next to the value of the copied node that the original node's next points to 
            oldToNew[cur].random = oldToNew[cur.random] 
            cur = cur.next
        return oldToNew[head]