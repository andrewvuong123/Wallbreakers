class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # General Idea: Can iterate through all the rows, columns and subboxes and add to set to check.
        
        valid = set()
        
        # Check each row
        for row in range(9):
            valid.clear()
            for col in range(9):
                position = board[row][col]
                if position in valid and position != ".":
                    return False
                valid.add(position)
        
        # Check each column
        for col in range(9):
            valid.clear()
            for row in range(9):
                position = board[row][col]
                if position in valid and position != ".":
                    return False
                valid.add(position)
                
        # Check each sub-box
        for i in (0, 3, 6): # each subbox within a col
            for j in (0, 3, 6): # each subbox within a row
                valid.clear()
                for row in range(i, i+3):
                    for col in range(j, j+3):
                        position = board[row][col]
                        if position in valid and position != ".":
                            return False
                        valid.add(position)
        return True
                