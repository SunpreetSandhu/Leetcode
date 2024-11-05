'''
Intuition:
The goal of this problem is to verify if a 9x9 sudoku board i valid accoding to the rules, which are:
    1) each row cant have a repeating num
    2) each col cant have a repeating num
    3) each 3x3 sub grid box cant have a repating num
We can use a hashmap to track these conditions. We'll have 3 hashmaps, one for rows, one for cols, and one for squares. The rows will have key = row, val = num, cols will have key = col, val = num and the square will have key = (r//3,c//3), val = num. We have tuples for each square, for ex the top left square will be (0,0) and the bottom right will be (2,2)

Approach:
1) initialize the hashmaps as defaultdicts for rows,cols,square, since we need to check a key prior to it existing to avoid key error we cant just do {}.
2)loop through each number from row and collumn
    a) Check if you see a '.', if so just continue to the next num
    b) If a number is encountered we need to check if that number does not exist in any of our hashmaps, row[r], col[c] and square[r//3,c//3], and if it does already exist in these hashmaps, we return false since we broke the rules
    c) add the elements in all hashmaps (use add and not = since we will be adding multiple values per key)
3) return True after checking all values

Time Complexity:
O(1) - Since we iterate thorugh each cell in a 9x9 board the the time complexity is O(9^2), or O(1)

Space Complexity:
O(1) - space of hashmap is constant and not dependent on input size as board is always 9x9
'''

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r]
                or board[r][c] in cols[c]
                or board[r][c] in square[(r//3,c//3)]
                ):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                square[(r//3,c//3)].add(board[r][c])
        return True


        