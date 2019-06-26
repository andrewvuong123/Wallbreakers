class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return 0
        
        # helper function that will change all Os at/connecting at the border to "-"
        def dfs(row, col):
            if not 0 <= row < len(board) or not 0 <= col < len(board[0]) or board[row][col] != 'O':
                return
            board[row][col] = "-"
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
            
        row = len(board)
        col = len(board[0])
        
        for y in range(row):
            for x in range(col):
                if y in {0, row-1} or x in {0, col-1} and board[y][x] == "O":
                    dfs(y, x)
        
        for y in range(row):
            for x in range(col):
                if board[y][x] == "-":
                    board[y][x] = "O"
                elif board[y][x] == "O":
                    board[y][x] = "X"
                    
        
        