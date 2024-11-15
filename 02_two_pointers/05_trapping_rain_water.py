'''
Intuition:
The problem involves finding how much water can be trapped between bars represented by an array, where each element of this array represents the height of the bar. The amount of water trapped at each individual index is represented by the MINIMIMUM (bottleneck), of the maximum of either the left or right side of this index, subtracted by the height at that index itself

Approach:
1) Use 2 pointer technique with l and r starting at leftmost and rightmost index of the array
2)Track the maxleft from the left, up to and including the current l, and maxright from the right up to and including the current r.These will initailly be the values of bars at leftmost and rightmost end of the array represented by l and r 


3)While l and r do not overlap (i.e., l < r):
    a) If maxLeft is less than or equal to maxRight:
        i)Move the left pointer (l) to the right (increment it).
        ii)Update maxLeft if necessary (i.e., set it to the maximum of maxLeft and height[l]).
        iii)Calculate the water trapped at index l as maxLeft - height[l] (will be 0 if we're currently at max) and add it to the total water.

    b)If maxRight is less than maxLeft:
        i)Move the right pointer (r) to the left (decrement it).
        ii)Update maxRight if necessary (i.e., set it to the maximum of maxRight and height[r]).
        iii)Calculate the water trapped at index r as maxRight - height[r] (will be 0 if we're currently at max) and add it to the total water.
4)Return the total water

Time complexity: O(n) -> just traversing array once
Space complexity: O(1) -> no extra memory, just pointers
'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        min max left, max right, - height[i]
        [4,2,0,3,2,5]
        ml = 4, mr = 
        """
        l, r = 0, len(height) -1
        maxLeft, maxRight = height[l], height[r]
        water = 0

        while l<r:
            if maxLeft<= maxRight:
                l+=1
                maxLeft = max(maxLeft, height[l])
                water += maxLeft - height[l]
            else:
                r-=1
                maxRight = max(maxRight, height[r])
                water += maxRight - height[r]
        return water
