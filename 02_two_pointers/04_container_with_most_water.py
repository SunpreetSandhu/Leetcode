'''
Intuition:
The problem requires finding 2 vertical lines from an array that together, with the x axis form a 'container' capable of holding the maximum amount of water. Essentially we are finding the max AREA of a rectangle. A brute force sol'n would be checking every pair which is O(n^2), but we will use two pointer, where we will be calculating the product of the shorter of the 2 pointers and the distance between them. At each step we will move the shorter of the 2 pointers

Apporach:
1)Initially define area as 0, left and right pointer at first and last index respectively
2) Loop until left doesn't cross right
    a)If the left pointer value is <= right pointer value, we will calculate the area as left pointer val * (r-l), where r-l is the distance between the 2. We will then calculate if this value is larger than the current maxArea. Finally we will increment l
    b)If the right pointer value is < right pointer value, we will calculate the area as right pointer val * (r-l), where r-l is the distance between the 2. We will then calculate if this value is larger than the current maxArea. Finally we will decrement r
3)Return the maximum area

Time Complexity: O(n) -> looping through list one pass
Space Complexity: O(1) -> no extra mem

'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        l =0
        r = len(height)-1
        while l<r:
            if height[l]<=height[r]:
                curArea = height[l] * (r-l)
                area = max(curArea, area)
                l+=1
            else:
                curArea = height[r] * (r-l)
                area = max(curArea,area)
                r-=1
        return area
            


        