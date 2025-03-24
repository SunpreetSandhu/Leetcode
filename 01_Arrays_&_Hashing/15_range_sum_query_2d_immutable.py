'''
Intuition:
We need to efficiently compute the sum of elements in a submatrix defined by 2 user coordinates. A brute force approach will iterate through all elements in the submatrix, but this will be too slow for large matrices and frequent calculations. Instead we can precompute a prefix sum matrix (sumMat), where each entry at (r,c), stores the sum of elements from (0,0) to (r,c). This allows us to answer the sum queries in O(1) time by using a trick that will eliminate unnecessary regions. The total sum we will have calculated at sumMat[r2][c2] will include some unwanted areas. 	We will subtract the sum of the row above the target region (r2-1,c2) and subtract the sum of the column to the left (r2,c2-1). The top left corner gets subtracted twice so to make it up we add it once (r1-1,c1-1)

Approach:
1) Precompute sumMat
    a)Fill a matrix sumMat with all 0s, and include an extra row and collum to deal with cases where we are using the top row / left most column.
    b)Compute prefix sums
        i)Iterate row wise over the input matrix
        ii)Maintain a running prefix sum for the row initially 0
        iii)Add the current value at the current row and column into the prefix accumulator
        iv)Update the sumMat matrix at (r+1,c+1) (the +1 is since we are using an extra row and column) to row wise prefix at the current (r,c) plus the prefix of the value above in sumMat (r,c+1) ensuring all values from the rows above are included.
2) Query sumRegion in O(1)
    a) Adjust r1, c1, r2, and c2 by adding 1 to each, as the prefix sum matrix sumMat has an extra row and column.
    b)Calculate bottomRight = sumMat[r2][c2], which represents the sum of all values from (0,0) to (r2, c2) but includes unwanted values outside the subarray.
    c) Calculate above = sumMat[r1-1][c2], which represents the sum of the rows above the top-right corner of the subarray. Subtract this to eliminate those values.
    d)Calculate left = sumMat[r2][c1-1], which represents the sum of the columns to the left of the bottom-left corner of the subarray. Subtract this to eliminate those values.
    e)Calculate topLeft = sumMat[r1-1][c1-1], which was subtracted twice during the previous steps, so add it back once to correct the result.

Time Complexity: O(1) for each query, O(n^2) for the initial prefix sum setup
Space Complexity: O(m*n) -> Where m is the number of rows in the input matrix and n is the number of columns.
'''

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumMat = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.sumMat[r][c + 1]
                self.sumMat[r + 1][c + 1] = prefix + above
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        bottomRight = self.sumMat[r2][c2]
        above = self.sumMat[r1 - 1][c2]
        left = self.sumMat[r2][c1 - 1]
        topLeft = self.sumMat[r1 - 1][c1 - 1]
        return bottomRight - above - left + topLeft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)