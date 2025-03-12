'''
Intuition: 
The goal is to design a HashMap using chaining to handle collisions. Each key is mapped to a bucket using a hash function and collisions are resolved by storing key-value pairs in a linked list within each bucket. This approach ensures efficient insertion, retrieval, and deletion by distributing keys across multiple buckets.

Approach:
1) Initialize an array (self.hm) of linked lists (buckets) with a fixed size of 10^4. Each bucket has a dummy head node to simplify insertion and deletion.
2)Use a hash function (key % len(self.hm)) to map keys to buckets
Put: Traverse the linked list in the mapped bucket. If the key exists, update its value; otherwise append a new node to the end of the linked list.
Get: Traverse the LL to find the key, return its value or -1 if not found.
Remove: Traverse the LL to find and remove the node with target key.

Time complexity:
O(n/k) -> n is the number of keys (up to 10^4 calls), k is the number of buckets (10^4 in our implementation). In the worst case all keys get stored in one bucket so k is 1 and time complexity becomes O(n). On average it will just be O(1)

Space Complexity:
O(k+m) -> k is number of buckets, m is the number of UNIQUE keys
'''

class ListNode():
    def __init__(self, key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap(object):

    def __init__(self):
        self.hm = [ListNode() for i in range(10**4)]
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        index = key % len(self.hm)
        cur = self.hm[index]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key,value)

        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        index = key % len(self.hm)
        cur = self.hm[index]
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = key % len(self.hm)
        cur = self.hm[index]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        
        

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)