'''
Intuition:
Goal is to design a hashset using a hash table with chaining to handle the collisions. Each key is mapped to a bucket using a hash function and collisions (multiple keys in the same bucket), are resolved by storing elements in a linked list within each bucket.

Appraoch:
Buckets/Chaining
    a)Initialize an array (self.set) of linked lists (buckets). Each bucket has a dummy head node to simplify insertion and deletion. We have a fixed number of bucked 10^4 which matches the max key value
    b)Use a hash function (key%len(self.set)) to map keys to buckets
    c)Add -> Traverse the linked list in the mapped bucket. If the key is not present append it to the end
    d) Remove -> Traverse the linked list to find and remove the key
    e) Contains -> Traverse the linked list and if the key exists in the mapped bucket return true, false otherwise

Time Complexity: 
O(1) on average, since collisions are rare
O(k) on worst case, where k is elements in each bucket

Space Complexity:
O(m + k) -> m is space of the buckets (10^4), k is keys stored in bucket

'''

class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet(object):
    def __init__(self):
        self.set = [ListNode(0) for i in range(10**4)]


        

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = key % len(self.set)
        cur = self.set[index]
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """

        index = key % len(self.set)
        cur = self.set[index]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        index = key % len(self.set)
        cur = self.set[index]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)