
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None
        Do not return anything, modify board in-place instead.
        """
        
        # Create sets to track used numbers
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        # Step 1: Initialize the sets with existing numbers
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)
        
        # Step 2: Backtracking function
        def backtrack():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        box_index = (r // 3) * 3 + (c // 3)
                        
                        for num in "123456789":
                            if (num not in rows[r] and
                                num not in cols[c] and
                                num not in boxes[box_index]):
                                
                                # Place number
                                board[r][c] = num
                                rows[r].add(num)
                                cols[c].add(num)
                                boxes[box_index].add(num)
                                
                                # Recurse
                                if backtrack():
                                    return True
                                
                                # Undo (Backtrack)
                                board[r][c] = "."
                                rows[r].remove(num)
                                cols[c].remove(num)
                                boxes[box_index].remove(num)
                        
                        return False
            return True
        
        backtrack()
